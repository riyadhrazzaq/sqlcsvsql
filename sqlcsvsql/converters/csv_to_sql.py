import csv
import logging
import sys

config = {}
output = {}
logger = logging.getLogger(__name__)


def run(table_name, file_name, is_multiline=False, output_file=None, surround=None):
    """
    driver method.

    Parameters
    ----------
    table_name: str
        name of the table to use in DML
    file_name: str
        input csv file
    is_multiline: bool
        whether to generate multiple insert statements or single one.
    output_file: str
        output filepath with extension
    surround: str
        quotation flags for VALUES (...) in generated sql

    Returns
    -------
    Nothing. Saves the file on disk
    """
    if output_file is None:
        output_file = file_name + ".sql"
    config["table"] = table_name

    table = read_csv(file_name)
    config["columns"] = list(table[0].keys())
    config["is_multiline"] = is_multiline
    output[config["table"]] = {"values": [], "insert_into": ""}
    setup_quote_chars(surround)
    write_to_sql(output_file, prepare_sql(table))


def setup_quote_chars(surround):
    config["quote"] = {}
    if surround is not None:
        surrounds = surround.split(",")
        if len(surrounds) != len(config["columns"]):
            logger.error(
                "surround parameter(s) %s does not match columns %s",
                len(surrounds),
                len(config["columns"]),
            )
            sys.exit(0)

        for idx, s in enumerate(surrounds):
            config["quote"][config["columns"][idx]] = "'"
            if s == "n":
                config["quote"][config["columns"][idx]] = ""
    else:
        for col in config["columns"]:
            config["quote"][col] = "'"


def read_csv(file_name):
    """
    read csv

    Returns
    -------
    rows: List[Dict]
        list of dict. each dict contains csv in {key:value} format
    """
    rows = []
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    return rows


def write_to_sql(file_name, content):
    with open(file_name, "w") as f:
        f.write(content)


def prepare_insert_header_statement(table, cols):
    """
    Returns first-half of INSERT DML, i.e `INSERT INTO TABLE (COLUMN...) VALUES`
    """
    cols_sql = f"({', '.join([c.strip() for c in cols])})"
    return f"INSERT INTO {table} {cols_sql} VALUES"


def format_value(value, quote):
    """
    decides the following for each values
        - null or not
        - use quotation or not
    """
    if value == "null":
        return value
    return quote + str(value) + quote


def prepare_statement(values):
    values_sql = f"""({', '
        .join([format_value(v, config['quote'][config['columns'][i]]) for i, v in enumerate(values)])})"""
    return values_sql


def prepare_values(line):
    """
    converts line in a csv to sql
    """
    table_name = config["table"]
    values = []
    for k in config["columns"]:
        values.append(line[k])
    statement = prepare_statement(values)
    output[table_name]["values"].append(statement)


def prepare_sql(table):
    """Generates the sql given a csv table"""
    sql = ""
    for row in table:
        prepare_values(row)
    insert_statement = prepare_insert_header_statement(
        config["table"], config["columns"]
    )
    if not config["is_multiline"]:
        sql = ", ".join(output[config["table"]]["values"])
        sql = insert_statement + " " + sql + ";"
        return sql

    for v in output[config["table"]]["values"]:
        sql = sql + "\n" + insert_statement + " " + v + ";"
    return sql
