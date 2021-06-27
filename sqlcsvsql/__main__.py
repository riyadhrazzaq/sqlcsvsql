import re
import argparse
import logging

from sqlcsvsql.converters import sql_to_csv, csv_to_sql

REGEX_CSV = r".csv$"
REGEX_SQL = r".sql$"

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filepath", help="SQL or CSV file path")
parser.add_argument("-t", "--table-name", help="Table name for csv file")
parser.add_argument("-o", "--output", help="Output filepath. Must end with extension")
parser.add_argument(
    "-m",
    "--statement_mode",
    help="single or multiline DML to generate",
    choices=("single", "multi"),
)
parser.add_argument(
    "-s",
    "--surround",
    help="""surround values with single quote. For a CSV with columns A,B,C 
    if only B column's values should be surrounded with quotes, then use 
    ```--surround n,y,n```. By default, all values are surrounded. 
    """,
    choices=("y", "n"),
)


def main(arguments=None):
    logging.basicConfig(format="[%(levelname)s %(asctime)s %(name)s]: %(message)s")

    if arguments is None:
        parser.print_help()

    if arguments.filepath:
        if file_type(arguments.filepath) == "sql":
            sql_to_csv.run(arguments.filepath, arguments.output)
        elif file_type(arguments.filepath) == "csv":
            csv_to_sql.run(
                arguments.table_name,
                arguments.filepath,
                arguments.statement_mode == "multi",
                arguments.output,
                arguments.surround
            )


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


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
