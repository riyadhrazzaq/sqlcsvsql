insert_stmt = r""
table_name = r"(?<=insert[\W]into[\W])(\w+)"
column_names = r"(\([-'`\d\w, ]+\))(?:\W+)(?:values)"
values_starting_position = r"(?:insert[\W]+into[\W]+[ \w\d_]+\([,\w\d' ]+\)[\W]+)(?:values[ ]+)"
comma_between_multiple_values = r"(?:\)[\W]*)(,)(?:[\W]*\()"

round_br_op = '('
round_br_cl = ')'

curly_br_op = '{'
curly_br_cl = '}'

single_quote = "'"
double_quote = '"'
comma = ','
semi_colon = ';'

text = """INSERT INTO tablename (id, name, age) values (1, 'abdu_ds',  null);
INSERT INTO tablename (id, name, age) values (1, 'abdu_ds',  null);
INSERT INTO tablename (id, name, age) values (1, 'abdu_ds',  null);

INSERT INTO tablename (id, name, age) values (1, 'abdu_ds',  null),(1, 'abdu_ds',  null),
(1, 'abdu_ds',  null);"""

multiline = "INSERT INTO tablename (id, name, age) values (1, 'a(bd,)u_ds',  null),(1, 'abdu_ds',  null),\
(1, 'abdu_ds',  null);"

"""
rules
1. if , without last item quote in b : make tuple
2. if ( with last item in b is quote: text
3. if ) with last item in b is quote: text
4. if quote with last item in b is quote: pop, text
5. if ) with last item in b is (: tuple, pop
6. if , without any item in b, do nothing
tuple = (1, a(bd,)u_ds)
b = [(]
c = )
str = null
"""