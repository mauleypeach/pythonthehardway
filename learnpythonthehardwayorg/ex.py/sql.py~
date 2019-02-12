#!/usr/bin/python



import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
try:
   connection = mysql.connector.connect(host='localhost',
           database='pets_db',
                             user='mprak',
                             password='Padomei')
   sql_insert_query = """ INSERT INTO `pets_db`
                          (`id`, `name`, `birth_date`, `age`) VALUES (1,'Harry','2000-05-11', 18)"""
   cursor = connection.cursor()
   result  = cursor.execute(sql_insert_query)
   connection.commit()
   print ("Record inserted successfully into pets_db table")
except mysql.connector.Error as error :
    connection.rollback() #rollback if any exception occured
    print("Failed inserting record into pets_db table {}".format(error))
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


