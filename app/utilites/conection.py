import psycopg2

class Conection:
    @staticmethod
    def conect():
        server = 'batyr.db.elephantsql.com'
        #port = 5432
        db_name = 'onryyemf'
        user_name = 'onryyemf'
        password = 'vAiidLCoyYoIjo8ii9xqQNwLrIply_1H'
        conn = psycopg2.connect(host= server , database=db_name , user= user_name, password=password)
        print ("conexion a base de datos ok 1")
        return conn

