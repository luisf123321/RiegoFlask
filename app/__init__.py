from flask import Flask
#from mod1 import mod1
from .auth import auth
from .config import Config
from .cultivos import cultivo
from .finca import finca
from .lotes import lote
from .extensions import jwt
from .prediccion import prediction
from .clima import clima
from .riego import riego
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    #login_manager.init_app(app)
    #Conection.conect()
    #cor = Conection.conect().cursor()
    jwt.init_app(app)
    #app.register_blueprint(mod1)
    app.register_blueprint(auth)
    app.register_blueprint(cultivo)
    app.register_blueprint(finca)
    app.register_blueprint(lote)
    app.register_blueprint(prediction)
    app.register_blueprint(clima)
    app.register_blueprint(riego)
    return app