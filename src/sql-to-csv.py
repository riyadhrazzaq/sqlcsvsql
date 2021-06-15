from sql_parser.parsers import Parser
import sql_parser.parsers as sp

config = {

}


def run(file_path):
    with open(file_path, 'r') as file:
        sql = file.read()
    p = Parser(sql, True)
    print("original file\n", p.sql)
    print("table names\n", sp.get_table_name(p.sql))
    print("values\n", sp.parse_multiple_value_statement(p.sql))
    p.parse()
    print("output\n", p.output["values"])


run("input.sql")
