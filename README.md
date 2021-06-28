# sql-to-csv-to-sql

A Simple Command Line Utility for converting SQL INSERT statements to CSV and vice versa.

# Installation

`pip install sqlcsvsql`

# Usage

```
usage: __main__.py [-h] [-f FILEPATH] [-t TABLE_NAME] [-o OUTPUT] [-m {single,multi}] [-s {y,n}]

optional arguments:
  -h, --help            show this help message and exit
  -f FILEPATH, --filepath FILEPATH
                        SQL or CSV file path
  -t TABLE_NAME, --table-name TABLE_NAME
                        Table name for csv file
  -o OUTPUT, --output OUTPUT
                        Output filepath. Must end with extension
  -m {single,multi}, --statement_mode {single,multi}
                        single or multiline DML to generate
  -s {y,n}, --surround {y,n}
                        surround values with single quote. For a CSV with columns A,B,C if only B column's values should be surrounded with quotes, then use ```--surround n,y,n```. By default, all values are
                        surrounded.
```

## Convert `SQL` to `CSV`

```
python -m sqlcsvsql -f file.sql
```

the converted file will be saved in the same directory with file name `file.sql.csv`

## Convert `CSV` to `SQL`

```
python -m sqlcsvsql -f file.csv -t example_table -m single
```

the converted file will be saved in the same directory with file name `file.csv.sql`
