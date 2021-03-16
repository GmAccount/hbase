import happybase

connection = happybase.Connection('127.0.0.1')
table = connection.table('emp')



table.put(b'row-key01', {b'personal data:name': b'value1',b'professional data:salary': b'value2'})



#row = table.row(b'1')
row = table.row(b'1')
print(row)

#print(row[b'personal:data'])  # prints 'value1'


"""
for key, data in table.rows([b'row-key01', b'row-key02']):
    print(key, data)  # prints row key and data for each row
"""
for key, data in table.scan(row_prefix=b'row'):
    print(key, data)  # prints 'value1' and 'value2'

row = table.delete(b'row-key02')
