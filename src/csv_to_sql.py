import pandas as pd

config = {}
output = {}

def run(table_name, file_name):
	config["table"] = table_name
	config["file_name"] = file_name

table = pd.read_csv(config["file_name"])
config["columns"] = list(table.columns.values)
config["single_insert"] = True
output[config["table"]] = {
	"values": [],
	"insert_into": ""
}

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
	table = config["table"]
	cols = config['columns']
	values = list(line)
	statement = prepare_statement(values)
	output[table]["values"].append(statement)

def prepare_sql():
	sql = ""
	table.apply(prepare_values,axis=1)
	insert_statement = prepare_insert_header_statement(config["table"], config["columns"])
	if not config["single_insert"]:
		sql = ", ".join(output[config["table"]]["values"])
		sql = insert_statement + " " + sql
		return sql

	for v in output[config["table"]]["values"]:
		sql = sql + "\n" + insert_statement + " " + v
	return sql

print("columns: ", config["columns"])
print("table name: ", config["table"])
print(prepare_sql())