import mysql.connector

def connect_database():
    cnx = mysql.connector.connect(user='root', password='Loc2002_bl',
                                host='127.0.0.1',
                                database='trading')
    cnx.close()
    return cnx