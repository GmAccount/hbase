import happybase



connection = happybase.Connection('127.0.0.1')



"""
# create table 
connection.create_table('book',
{'cf_author': dict(max_versions=4),
 'cf_book_info': dict()
}
)
"""

# cnx to table
table = connection.table('book')



# insert 3 rows with column family cf_book_info
table.put(b'1', {b'cf_book_info:title': b'Faster than the speed love',b'cf_book_info:description': b'long book about the love'})
table.put(b'2', {b'cf_book_info:title': b'Long day',b'cf_book_info:description': b'Story about Monday'})
table.put(b'3', {b'cf_book_info:title': b'Flaying car',b'cf_book_info:description': b'Novel about airplans'})


# adding a second column family cf_author
table.put(b'1', {b'cf_author:fname': b'Brian',b'cf_author:lname': b'Dog'})
table.put(b'2', {b'cf_author:fname': b'Emily',b'cf_author:lname': b'Blue'}) 
table.put(b'3', {b'cf_author:fname': b'Phil',b'cf_author:lname': b'High'}) 


# recuperer record avec ID=1
row = table.row(b'1')

# 
row2 = table.row(b'2')
print("Le titre de livre (ID=2) est :",row2[b'cf_book_info:title'])  
print("La description de livre (ID=2) est :",row2[b'cf_book_info:description'])




for key, data in table.scan():

    if data[b'cf_book_info:title'] == b'Long day':
        print("---------")
        print(key,data[b'cf_book_info:title'])
        print("------")
        table.put(key, {b'cf_author:lname': b'Happy'})



row_changed = table.row(b'2')
print(row_changed)



##row = table.delete(b'row-key02')
