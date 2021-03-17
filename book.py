import happybase



connection = happybase.Connection('127.0.0.1')


"""
connection.create_table('book',
{'cf_author': dict(max_versions=4),
 'cf_book_info': dict()
}
)
"""
table = connection.table('book')

table.put(b'1', {b'cf_book_info:title': b'Faster than the speed love',b'cf_book_info:description': b'long book about the love'})



#row = table.row(b'1')
#row = table.row(b'1')
#print(row)
#print(row[b'personal:data'])  # prints 'value1'


"""
for key, data in table.rows([b'row-key01', b'row-key02']):
    print(key, data)  # prints row key and data for each row

for key, data in table.scan(row_prefix=b'row'):
    print(key, data)  # prints 'value1' and 'value2'

row = table.delete(b'row-key02')
"""
