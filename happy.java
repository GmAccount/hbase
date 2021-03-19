import static org.apache.hadoop.hbase.util.Bytes.toBytes;


import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.client.HBaseAdmin;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;


import static org.apache.hadoop.hbase.util.Bytes.*;


public class happy {
	public static void main(String[] args) throws IOException {

		
		Configuration conf = HBaseConfiguration.create();
		HBaseAdmin admin = new HBaseAdmin(conf);
		
		String name = "bookJava";
		byte [] tableName = toBytes(name);
		HTableDescriptor table = new HTableDescriptor(tableName);
		HColumnDescriptor family1 = new HColumnDescriptor(toBytes("cf_author"));
		table.addFamily(family1);
		
		HColumnDescriptor family2 = new HColumnDescriptor(toBytes("cf_book"));
		table.addFamily(family2);		
		
		System.out.println("Table "+name+" exist: " + admin.tableExists(tableName)) ;
		System.out.println("Creating "+name+" table...");
		admin.createTable(table);
		System.out.println("Table "+name+" exist: " + admin.tableExists(tableName)) ;
		
		
		HTable hTable = new HTable(conf, "bookJava");
		
		Put put1 = new Put(toBytes("1"));
		put1.add(toBytes("cf_author"), toBytes("fname"), toBytes("fname01"));
		put1.add(toBytes("cf_author"), toBytes("lname"), toBytes("lname02"));
		hTable.put(put1);
		
		hTable.close();
		
		
	}
}




