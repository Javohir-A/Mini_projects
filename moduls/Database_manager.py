import mysql.connector

class DatabaseManager:
    def __init__(self,host = 'localhost', user = "root", passwd = None, database = None) :
        self.connection = self.connect_mysql(host,user,passwd, database)
        self.cursor = self.connection.cursor()
        
    def connect_mysql(self, host, user, passwd, database):
        try:
            connection = mysql.connector.connect(
                host = host,
                user = user,
                passwd = passwd,
                database = database
            )
            return connection
        except mysql.connector.Error as err:
            print(f'Error connceting to mysql database: {err}')
            exit()
            
    def fetch_all(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute_query(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f'Cannot execute query: {err}')
            exit()
    def close_connection(self):
        self.cursor.close()
        self.connection.close()

