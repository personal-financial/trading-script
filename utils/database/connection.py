import mysql.connector

class DatabaseConnection:
    def __init__(self):
        self.connection = None
    
    def connect(self):
        self.connection = mysql.connector.connect(user='root', password='Loc2002_bl',
                                host='127.0.0.1',
                                database='trading')
    def get_connection(self):
        return self.connection
        
    def close(self):
        self.connection.close()