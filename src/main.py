import re
import argparse

import sql_to_csv
import csv_to_sql


REGEX_CSV = r".csv$"
REGEX_SQL = r".sql$"

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filepath", help="sql or csv file path")
parser.add_argument("-t", "--table_name", help="table name for csv file")
parser.add_argument("-m", "--statement_mode", help="single or multiline DML to generate", choices=("single", "multi"))


def main(arguments):
    if arguments.filepath:
        if file_type(arguments.filepath) == "sql":
            sql_to_csv.run(arguments.filepath)
        elif file_type(arguments.filepath) == "csv":
            csv_to_sql.run(arguments.table_name, arguments.filepath, arguments.statement_mode == "multi")


def file_type(filename):
    csv_pattern = re.compile(REGEX_CSV, re.IGNORECASE)
    sql_pattern = re.compile(REGEX_SQL, re.IGNORECASE)

    m = csv_pattern.search(filename)
    if m:
        return "csv"
    m = sql_pattern.search(filename)
    if m:
        return "sql"
    return None


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)