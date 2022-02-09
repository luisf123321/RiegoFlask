import pandas as pd 
from .utilites.conection import Conection

class Users:
    @staticmethod
    def getUsers():
        cor = Conection.conect().cursor()
        sql = "SELECT * FROM usuario"
        result = pd.read_sql_query(sql, Conection.conect())
        print (result)