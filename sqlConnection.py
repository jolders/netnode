import os.path
from PySide6 import QtWidgets, QtSql
from PySide6.QtSql import QSqlQuery, QSqlDatabase
from PySide6.QtWidgets import QMessageBox


class SqlDataConnection:
    def __init__(self):
        super(SqlDataConnection, self).__init__()
        self.create_connection()

    def create_connection(self):
        path = './devices_db.db'
        check_file = os.path.isfile(path)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('devices_db.db')

        if check_file == False:
            print("Check file is FALSE")
            button = QMessageBox.question(None, "Unable to find the database file", "The Devices table relies on a 'devices_db.db' file.\n\n The file was not found in the root location.\n\nClick Yes to create a new db file with sample data.\n\nClick No to exit (donot create a new DB file)\n", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if button == QMessageBox.Yes:
                print("Yes was pressed")

                #db = QSqlDatabase.addDatabase('QSQLITE')
                # db.setDatabaseName('devices_db.db')

                if db.isOpen() == False:
                    print("(A sqlConnection) | The database connection is about to be opened.")

                db.open()

                if db.isOpen() == False:
                    print("(B sqlConnection) | The database is not open and it should be.")

                if db.isOpen() == True:
                    print("(C sqlConnection) | The database connection now open.")


                query = QtSql.QSqlQuery()
                query.exec("""CREATE TABLE IF NOT EXISTS "devices" (
                'ID'	INTEGER,
                'Hostname'	TEXT,
                'IPaddress'	TEXT,
                'Username'	TEXT,
                'Password'	TEXT,
                'Location'	TEXT,
                'Description'	TEXT,
                PRIMARY KEY('ID' AUTOINCREMENT));""")

                '''
                confirm = QMessageBox.question(None, "Sample table data ?", "Do you want to load some sample data ?\n (You can use Update and Delete) \n     Click Ok to exit.", QMessageBox.Yes | QMessageBox.No)
                if confirm == QMessageBox.Yes:
                    print("Yes was pressed - insert into table SQL statement")
                    sql_query = "INSERT INTO devices (Hostname, IPaddress, Username, Password, Location, Description) VALUES (?, ?, ?, ?, ?, ?)"
                    self.execute_query_with_params(sql_query, ['Hostname_1', '1.1.1.1', 'Usr1', 'Pass1', 'Loc1', 'Desc1'])
                    self.execute_query_with_params(sql_query, ['Hostname_2', '2.2.2.2', 'Usr2', 'Pass2', 'Loc2', 'Desc2'])
                    self.execute_query_with_params(sql_query, ['Hostname_3', '3.3.3.3', 'Usr3', 'Pass3', 'Loc3', 'Desc3'])
                    self.execute_query_with_params(sql_query, ['Hostname_4', '4.4.4.4', 'Usr4', 'Pass4', 'Loc4', 'Desc4'])
                    self.execute_query_with_params(sql_query, ['Hostname_5', '5.5.5.5', 'Usr5', 'Pass5', 'Loc5', 'Desc5'])

                else:
                    return True
                '''

                sql_query = "INSERT INTO devices (Hostname, IPaddress, Username, Password, Location, Description) VALUES (?, ?, ?, ?, ?, ?)"
                self.execute_query_with_params(sql_query, ['Hostname_1', '1.1.1.1', 'Usr1', 'Pass1', 'Loc1', 'Desc1'])
                self.execute_query_with_params(sql_query, ['Hostname_2', '2.2.2.2', 'Usr2', 'Pass2', 'Loc2', 'Desc2'])
                self.execute_query_with_params(sql_query, ['Hostname_3', '3.3.3.3', 'Usr3', 'Pass3', 'Loc3', 'Desc3'])
                self.execute_query_with_params(sql_query, ['Hostname_4', '4.4.4.4', 'Usr4', 'Pass4', 'Loc4', 'Desc4'])
                self.execute_query_with_params(sql_query, ['Hostname_5', '5.5.5.5', 'Usr5', 'Pass5', 'Loc5', 'Desc5'])

                db.close()

                if db.isOpen():
                    print("A isOpen = True")
                    db.close()
                else:
                    print("The db connection has been closed")

            else:
                print("No was pressed")

        elif check_file == True:
            print("Check file is TRUE")
            #QtWidgets.QMessageBox.information(None, "File exists", "Database file 'devices_db.db' is present in the root directory.\n\n     Click Ok to exit.", QtWidgets.QMessageBox.Ok)
        else:
            print("An error occured on checking if there is a database file existing")




    def execute_query_with_params(self, sql_query, query_values=None):
        print("I AM execute_query_with_params")
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        print(f"query = {query.prepare(sql_query)}")

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def add_new_transaction_query(self, hostname, ipaddress, username, password, location, description):
        sql_query = "INSERT INTO devices (Hostname, IPaddress, Username, Password, Location, Description) VALUES (?, ?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [hostname, ipaddress, username, password, location, description])

    def update_device(self, new_hostname, new_ipaddress, new_username, new_password, new_location, pte_description, id):
        query = QtSql.QSqlQuery()
        sql_query = f"UPDATE devices SET Hostname='{new_hostname}', IPaddress='{new_ipaddress}', Username='{new_username}', Password='{new_password}', Location='{new_location}', Description='{pte_description}' WHERE ID='{id}'"

        print(sql_query)
        query.prepare(sql_query)
        query.exec()
        #sql_query = "UPDATE devices SET Hostname=?, IPaddress=?, Username=?, Password=?, Location=?, Description=? WHERE ID=?"
        #self.execute_query_with_params(sql_query, [hostname, ipaddress, username, password, location, description, id])

    def create_new_device(self, hostname, ipaddress, username, password, location, pte_description):
        print(f"create_new_device Hostname is: {hostname}")
        print(f"create_new_device ipaddress is: {ipaddress}")
        print(f"create_new_device username is: {username}")
        print(f"create_new_device password is: {password}")
        print(f"create_new_device location is: {location}")
        #print(f"create_new_device description is: {description}")
        print(f"create_new_device description is: {pte_description}")

        query = QtSql.QSqlQuery()
        sql_query = f"INSERT INTO devices (Hostname, IPaddress, Username, Password, Location, Description) VALUES ('{hostname}', '{ipaddress}', '{username}', '{password}', '{location}', '{pte_description}')"
        query.prepare(sql_query)
        query.exec()



    # OPtion1 to setup Delete Formulate the SQL and directly send request command
    def delete_device(self, id):
        print(f"delete_transaction_query: ID = {id}")
        query = QtSql.QSqlQuery()
        sql_query = f"DELETE FROM devices WHERE ID={id}"
        query.prepare(sql_query)
        query.exec()
        return

    # OPtion2 to setup Delete
    '''
    def delete_device(self, id):
        print(f"Deleting record (delete_transaction_query) id= {id}")
        sql_query = "DELETE FROM devices WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])
    '''




