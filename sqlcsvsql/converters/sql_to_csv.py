from sqlcsvsql.sqlparsers.parsers import Parser


def run(file_path, output=None):
    if output is None:
        output = file_path + ".csv"
    with open(file_path, "r", encoding="utf8") as file:
        sql = file.read()
    p = Parser(sql, True)
    p.parse()
    p.to_csv(output)
