import unittest
import csv
import io

import sqlcsvsql.converters.sql_to_csv as s2c

CSV = ".csv"


class TestSQLToCSV(unittest.TestCase):
    def simple_sql(self):
        input_filepath = "tests/resources/input.sql"
        s2c.run(input_filepath)
        op_filepath = input_filepath + CSV
        expected_csv = """"id","created","deleted","last_updated","uuid_str","name_bn","name_en","created_by_id","updated_by_id","upazila_id","bbs_code","bbs_code_3digit","is_updated","municipality_id","weight"
"8253","2020-06-03 17:36:28","false","2020-06-03 17:36:28","2c01985a-d20c-4c3b-9348-e228938ce1ae","সুতারপাড়া","SUTARPARA","null","null","185","94","713","1","null","0"
"8254","2020-06-03 17:36:28","false","2020-06-03 17:36:28","d0808b7b-e7d3-4c70-8c53-38eee28e6ee6","ওয়ার্ড নং ০১","WARD NO. 01","null","null","185","1","1","1","108","0"
"8255","2020-06-03 17:36:28","false","2020-06-03 17:36:28","24c9a0d5-f63f-409c-ac61-fe323655a9eb","ওয়ার্ড নং ০২","WARD NO. 02","null","null","185","2","2","1","108","0"
"8256","2020-06-03 17:36:28","false","2020-06-03 17:36:28","fafe6da6-9a96-4b58-a49d-b1bdba49538c","ওয়ার্ড নং ০৩","WARD NO. 03","null","null","185","3","3","1","108","0"
"""
        expected_csv_dicts = []
        f = io.StringIO(expected_csv)
        with open(f) as csv_file:
            reader = csv.DictReader(csv_file)
            for obj in reader:
                expected_csv_dicts.append(obj)

        actual_csv_lines = []
        with open(op_filepath) as csv_file:
            reader = csv.reader(csv_file)
            for obj in reader:
                actual_csv_lines.append(obj)

        self.assertDictEqual(expected_csv_dicts[0], actual_csv_lines[0])
