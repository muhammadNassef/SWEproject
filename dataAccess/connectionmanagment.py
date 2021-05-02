import mysql.connector


class ConnectionManagment:

    @staticmethod
    def getConnection():
        return mysql.connector.connect(host='localhost', user='root', passwd='', database='store')


