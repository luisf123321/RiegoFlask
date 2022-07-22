import pandas as pd 
import psycopg2
import os
import sys
sys.path.append(os.path.abspath('..'))
from utilites.conexion import Conection

class tipo_identificacion:
    @staticmethod
    def getTipoIdentificacion():
        cor = Conection.conect()
        sql = "SELECT * FROM tipo_identificacion"
        print(sql)
        result = pd.read_sql_query(sql, con= cor)
        print(result)
        cor.close()
        return result