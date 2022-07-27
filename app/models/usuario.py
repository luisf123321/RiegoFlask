import pandas as pd 
from .utilites.conexion  import Conexion


import psycopg2


class Users:
    @staticmethod
    def getUsers():
        cor = Conection.conect()
        sql = "SELECT * FROM usuario"
        result = pd.read_sql_query(sql, con= cor)
        print(result)
        cor.close()
        #Conection.conect().close()
        return result

    @staticmethod
    def getUser(num_identificacion):
        str(num_identificacion)
        cur = Conection.conect()
        sql = "SELECT usu_numero_identificacion FROM usuario WHERE usu_numero_identificacion =  " + num_identificacion
        print(sql)
        result = pd.read_sql_query(sql, con= cur)
        print(type(result))
        return result

    @staticmethod
    def insertUser(username, apellido, num_identificacion, num_celular, direccion, nickname, password_hash,correo,tipo_identificacion):
        try:
            sql = "INSERT INTO usuario(usu_nombre, usu_apelliido, usu_numero_identificacion, usu_celular, usu_direccion, usu_user, usu_password, usu_correo, usu_tipo_identificacion) \
                values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            conn = Conection.conect()
            cor = conn.cursor()
            cor.execute(sql,(username, apellido ,num_identificacion, num_celular, direccion ,nickname , password_hash, correo, tipo_identificacion))
            conn.commit()
            print("Usuario registrado")
        except psycopg2.DatabaseError as error:
            print(error)
            #conn.rollback()
        finally:
            conn.close()
