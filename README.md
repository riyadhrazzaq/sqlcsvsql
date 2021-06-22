# sql-to-csv-to-sql
A Simple Command Line Utility for converting SQL statements to CSV and vice versa.

# Installation
`pip install `

# Usage
```
python -m sqlcsvsql OPTIONS
  -h, --help            show this help message and exit
  -f FILEPATH, --filepath FILEPATH
                        sql or csv file path
  -t TABLE_NAME, --table_name TABLE_NAME
                        table name for csv file
  -m {single,multi}, --statement_mode {single,multi}
                        single or multiline DML to generate
```
## Convert `SQL` to `CSV`
```
python -m sqlcsvsql -f file.sql
```
converted file will be saved in the same directory with file name `file.sql.csv`

## Convert `CSV` to `SQL`
```
python -m sqlcsvsql -f file.csv -t example_table -m single
```
converted file will be saved in the same directory with file name `file.csv.sql`
