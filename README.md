## start thrift server

[root@a06afe47321f bin]# ./hbase-daemon.sh start thrift
starting thrift, logging to /usr/local/hbase/hbase-1.1.2/bin/../logs/hbase--thrift-a06afe47321f.out

# check if started
[root@a06afe47321f bin]# jps
1 HMaster
1493 Jps
1447 ThriftServer
351 Main
[root@a06afe47321f bin]# pwd
/usr/local/hbase/hbase-1.1.2/bin

## Execution

[root@3b8aeb261c97 hbase]# python3 book.py
Le titre de livre (ID=2) est : b'Long day'
La description de livre (ID=2) est : b'Story about Monday'
---------
b'2' b'Long day'
------
{b'cf_author:fname': b'Emily', b'cf_author:lname': b'Happy', b'cf_book_info:description': b'Story about Monday', b'cf_book_info:title': b'Long day'}

