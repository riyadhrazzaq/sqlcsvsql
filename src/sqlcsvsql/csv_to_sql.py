import pandas as pd

config = {}
output = {}


def run(table_name, file_name, is_multiline=False):
    config["table"] = table_name

    table = pd.read_csv(file_name)
    config["columns"] = list(table.columns.values)
    config["is_multiline"] = is_multiline
    output[config["table"]] = {"values": [], "insert_into": ""}
    write_to_sql(file_name + ".sql", prepare_sql(table))


def write_to_sql(file_name, content):
    print(output[config["table"]]["values"])
    with open(file_name, "w") as f:
        f.write(content)


def prepare_insert_header_statement(table, cols):
    cols_sql = f"({', '.join([c.strip() for c in cols])})"
    return f"INSERT INTO {table} {cols_sql} VALUES"


def prepare_statement(values):
    values_sql = f"({', '.join([str(v) for v in values])})"
    return values_sql


def prepare_values(line):
    """
    converts line in a csv to sql
    """
    table_name = config["table"]
    values = list(line)
    statement = prepare_statement(values)
    output[table_name]["values"].append(statement)


def prepare_sql(table):
    sql = ""
    table.apply(prepare_values, axis=1)
    insert_statement = prepare_insert_header_statement(
        config["table"], config["columns"]
    )
    if not config["is_multiline"]:
        sql = ", ".join(output[config["table"]]["values"])
        sql = insert_statement + " " + sql + ";"
        return sql

    for v in output[config["table"]]["values"]:
        sql = sql + "\n" + insert_statement + " " + v + ";"
    print(sql)
    return sql
