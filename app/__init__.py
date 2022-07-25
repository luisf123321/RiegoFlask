from flask import Flask
#from mod1 import mod1
from .auth import auth
from .config import Config
from .cultivos import cultivo

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    #login_manager.init_app(app)
    #Conection.conect()
    #cor = Conection.conect().cursor()
    
    #app.register_blueprint(mod1)
    app.register_blueprint(auth)
    app.register_blueprint(cultivo)
    return app