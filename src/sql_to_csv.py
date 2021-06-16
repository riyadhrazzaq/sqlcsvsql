from sql_parser.parsers import Parser
import sql_parser.parsers as sp

config = {

}


def run(file_path):
    with open(file_path, 'r', encoding='utf8') as file:
        sql = file.read()
    p = Parser(sql, True)
    p.parse()
    print("output\n", p.output["values"])


run("input.sql")
