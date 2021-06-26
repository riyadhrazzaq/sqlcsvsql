from sqlcsvsql.sql_parser import Parser


def run(file_path):
    with open(file_path, "r", encoding="utf8") as file:
        sql = file.read()
    p = Parser(sql, True)
    p.parse()
    p.to_csv(file_path + ".csv")
