import mysql.connector
from mysql.connector import Error


class Factory:
    def __init__(self):
        self._erro = None

    def get_connection(self):
        con = None
        try:
            con = mysql.connector.connect(host='localhost', database='dados_erosao',
                                          user='root', password='123456789')
        except Error as erro:
            self._erro = erro
        return con
