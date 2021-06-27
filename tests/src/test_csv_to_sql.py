import unittest
import os

import sqlcsvsql.converters.csv_to_sql as c2s
from tests.src.hasher import Type, hash

print(os.getcwd())

CSV_PATH = "tests/resources/csv"
OUTPUT_PATH = "tests/outputs/actual"
EXP_PATH = "tests/outputs/expected"


class TestCSVToSQL(unittest.TestCase):
    def test_addresses(self):
        """
        test addresses.csv
        """
        filename = CSV_PATH + "/addresses.csv"
        output = OUTPUT_PATH + "/addresses.sql"
        expected = EXP_PATH + "/addresses.sql"

        c2s.run("addresses", filename, is_multiline=False, output_file=output)
        self.assertEqual(
            hash(expected, Type.SHA1).digest(), hash(output, Type.SHA1).digest()
        )


if __name__ == "__main__":
    unittest.main()
