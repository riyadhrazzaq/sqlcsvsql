import re

from . import reg_exp


class Parser:
    output = {"table_name": "", "values": [], "columns": []}

    def __init__(self, sql, multiple_stmt=False) -> None:
        self.sql = sql
        self.multiple_stmt = multiple_stmt

    def parse(self):
        self.output["table_name"] = get_table_name(self.sql)
        all_insert_statements = get_all_insert_stmt(self.sql)
        self.output["statements"] = all_insert_statements
        for statement in all_insert_statements:
            starting_positions = get_values_starting_pos(statement)
            for pos in starting_positions:
                partial_sql = statement[pos:]
                self.output["values"] += parse_multiple_value_statement(partial_sql)
                print(self.output["values"])
        return

    def to_csv(self):
        pass


def get_table_name(sql: str, multiple_stmt=False):
    """
    returns table name from sql. assumes only one table is in the sql
    """
    expression = re.compile(reg_exp.table_name, re.IGNORECASE)
    names = expression.findall(sql)
    if len(names) == 0:
        print("ERR! no table found")
    return names[0]


def get_values_starting_pos(sql: str):
    positions = []
    expression = re.compile(reg_exp.values_starting_position, re.IGNORECASE)
    iteration = expression.finditer(sql)
    if iteration is None:
        print("ERR! no values here")
    for match in iteration:
        positions.append(match.end())
    return positions


def parse_multiple_value_statement(sql: str):
    """
    1. if , without last item quote in b : make tuple
    2. if ( with last item in b is quote: text
    3. if ) with last item in b is quote: text
    4. if ' with last item in b is quote: pop, text
    5. if ) with last item in b is (: tuple, pop
    6. if , without any item in b, do nothing
    """
    list_values = []

    brackets = []
    current_substr = ""
    sub_str_list = []
    for c in sql:
        if c == reg_exp.comma:
            if len(brackets) == 0:
                continue
            if last_item(brackets) != reg_exp.single_quote:
                sub_str_list.append(current_substr.strip())
                current_substr = ""
                continue
        if c == reg_exp.round_br_op:
            if last_item(brackets) != reg_exp.single_quote:
                brackets.append(reg_exp.round_br_op)
                continue
        if c == reg_exp.round_br_cl:
            if last_item(brackets) == reg_exp.round_br_op:
                brackets.pop()

                sub_str_list.append(current_substr.strip())
                list_values.append(tuple(sub_str_list))

                sub_str_list = []
                current_substr = ""
                continue
        if c == reg_exp.single_quote:
            if last_item(brackets) == reg_exp.single_quote:
                brackets.pop()
                current_substr += reg_exp.single_quote
            else:
                brackets.append(reg_exp.single_quote)
            continue

        current_substr += c
    return list_values


def get_all_insert_stmt(sql: str):
    """
    :param sql: complete sql read from file
    :return: list of sql separated by `;`
    """
    brackets = []
    cursor = 0
    positions = []
    stmts = []
    for c in sql:
        cursor += 1
        if c == reg_exp.semi_colon:
            if len(brackets) == 0:
                positions.append(cursor)
                continue
        if c == reg_exp.single_quote:
            if last_item(brackets) == reg_exp.single_quote:
                brackets.pop()
            else:
                brackets.append(reg_exp.single_quote)
                continue

    positions.insert(0, 0)
    positions.append(len(sql))
    for idx in range(0, len(positions)-1):
        stmts.append(sql[positions[idx]:positions[idx+1]].strip())
    return stmts


def last_item(arr):
    if len(arr) > 0:
        return arr[-1]
    return ''
