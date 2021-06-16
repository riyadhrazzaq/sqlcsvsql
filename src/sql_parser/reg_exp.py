table_name = r"(?<=insert[\W]into[\W])(\w+)"
column_names = r"(\([-'`\d\w, ]+\))(?:\W+)(?:values)"
values_starting_position = r"(?:insert[\W]+into[\W]+[ \w\d_]+\([,\w\d' _\n]+\)[\W]+)(?:values[ \n]+)"
comma_between_multiple_values = r"(?:\)[\W]*)(,)(?:[\W]*\()"

round_br_op = '('
round_br_cl = ')'

curly_br_op = '{'
curly_br_cl = '}'

single_quote = "'"
double_quote = '"'
comma = ','
semi_colon = ';'
