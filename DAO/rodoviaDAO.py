from model.rodovia import Rodovia
from DAO.factory.factory import Factory
from mysql.connector import Error


class RodoviaDAO:
    def __init__(self):
        self._con = None
        try:
            connection = Factory()
            self._con = connection.get_connection()
        except Error as erro:
            print(f"O erro é no init da RodoviaDAO: {erro}")

    def find_all(self):
        dados = []
        sql_comand = 'SELECT * FROM erosao'
        cursor = self._con.cursor()
        try:
            rodovia = Rodovia()
            cursor.execute(sql_comand)
            linha = cursor.fetchone()
            while linha:
                rodovia.identi = linha[0]
                rodovia.concessionaria = linha[1]
                rodovia.sp = linha[2]
                rodovia.sentido = linha[3]
                rodovia.municipio = linha[4]
                rodovia.latitude = linha[5]
                rodovia.longitude = linha[6]
                rodovia.evento = linha[7]
                dados.append(dict(rodovia))
                linha = cursor.fetchone()
            lista_dados = []
            for dado in dados:
                lista_dados.append(dict(dado))
            return lista_dados
        except Error as erro:
            print(f"O erro aconteceu na função find_all : {erro}")
        finally:
            cursor.close()

    def find_by_id(self, identi):
        sql_comand = f"SELECT * FROM erosao WHERE id = {identi}"
        cursor = self._con.cursor()
        try:
            rodovia = Rodovia()
            cursor.execute(sql_comand)
            linha = cursor.fetchone()
            while linha:
                rodovia.identi = linha[0]
                rodovia.concessionaria = linha[1]
                rodovia.sp = linha[2]
                rodovia.sentido = linha[3]
                rodovia.municipio = linha[4]
                rodovia.latitude = linha[5]
                rodovia.longitude = linha[6]
                rodovia.evento = linha[7]
                linha = cursor.fetchone()
            return dict(rodovia)
        except Error as erro:
            print(f"O erro esta na função find_by_id: {erro}")
        finally:
            cursor.close()

    def delete_by_id(self, identi):
        sql_comand = f"DELETE FROM erosao WHERE id = {identi}"
        cursor = self._con.cursor()
        try:
            cursor.execute(sql_comand)
            self._con.commit()
            return print(f"O registro: {identi}, foi excluido com sucesso")
        except Error as erro:
            print(f"O erro esta na função delete_by_id: {erro}")
        finally:
            cursor.close()

    def create_rodovia(self, rodovia):
        sql_comand = """INSERT INTO erosao(concessionaria, sp, sentido, municipio, lat, lon, evento)
        VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        cursor = self._con.cursor()
        try:
            cursor.execute(sql_comand, (rodovia.concessionaria, rodovia.sp, rodovia.sentido, rodovia.municipio,
                                        rodovia.latitude, rodovia.longitude, rodovia.evento))
            self._con.commit()
        except Error as erro:
            print(f"O erro esta na função create_rodovia: {erro}")
        finally:
            cursor.close()

    def update_by_id(self, rodovia, identi):
        sql_comand = """UPDATE erosao SET concessionaria = %s, sp = %s, sentido = %s, municipio = %s,
        lat = %s, lon = %s, evento = %s WHERE id = %s"""
        cursor = self._con.cursor()
        try:
            cursor.execute(sql_comand, (rodovia.concessionaria, rodovia.sp, rodovia.sentido,
                                        rodovia.municipio, rodovia.latitude, rodovia.longitude,
                                        rodovia.evento, identi))
            self._con.commit()
        except Error as erro:
            print(f"O erro esta na função update: {erro}")
        finally:
            cursor.close()
