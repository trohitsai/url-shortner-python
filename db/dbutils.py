import MySQLdb
from variables import *

class dbutils():

    def get_db_conn(self):
        connection = MySQLdb.connect(host="localhost",  
        user=username,
        passwd=password,
        db=db)
        return connection

    def run_insert_query(self,arg_query):
        connection=self.get_db_conn()
        cur = connection.cursor()   
        cur.execute(arg_query)
        connection.commit()
        return cur.fetchall()
    
    def run_select_query(self,arg_query):
        connection=self.get_db_conn()
        cur = connection.cursor()   
        cur.execute(arg_query)
        row_count = cur.rowcount
        if row_count>0:
            return cur.fetchall()
        else:
            return False

    def get_old_url_from_new_url(self,arg_new_url):
        print ">> "+ arg_new_url
        data=self.run_select_query("select oldurl from us_table1 where newurl='"+arg_new_url+"'")
        #print data[0][0]
        if data:
            return data[0][0]
        else:
            return False

    def update_new_url_in_db(self,arg_old_url,arg_new_url,arg_date):
        print "in update"
        data=self.run_insert_query("INSERT INTO us_table1(oldurl,newurl,datecreated) VALUES('"+arg_old_url+"','"+arg_new_url+"','"+arg_date+"')")
        print data



