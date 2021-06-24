import csv

config = {}
output = {}


def run(table_name, file_name, is_multiline=False):
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

    Returns
    -------
    Nothing. Saves the file on disk
    """
    config["table"] = table_name

    table = read_csv(file_name)
    config["columns"] = list(table[0].keys())
    config["is_multiline"] = is_multiline
    output[config["table"]] = {"values": [], "insert_into": ""}
    write_to_sql(file_name + ".sql", prepare_sql(table))


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
