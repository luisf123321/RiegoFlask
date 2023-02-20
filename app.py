from flask import Flask, request, jsonify
#from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from app.models.usuario import User
from app.auth.routes import signup

from app import create_app

app = create_app()

CORS(app)


@app.route('/')
def hello_world():
    return jsonify("hello world")


@app.route('/prueba', methods=['POST'])
def prueba():
    arena = float(request.json.get("arena", None))
    limo = float(request.json.get("limo", None))
    arcilla = float(request.json.get("arcilla", None))
    tipo = ""
    if ((limo + 1.5*arcilla) < 15):
        tipo = "arenoso"
    elif ((limo + 1.5*arcilla >= 15) and (limo + 2*arcilla < 30)):
        tipo = "arenoso franco"
    elif ((arcilla >= 7 and arcilla < 20) and (arena > 52) and ((limo + 2*arcilla) >= 30) or (arcilla < 7 and limo < 50 and (limo+2*arcilla) >= 30)):
        tipo = "franco arenoso"
    elif ((arcilla >= 7 and arcilla < 27) and (limo >= 28 and limo < 50) and (arena <= 52)):
        tipo = "franco"
    elif ((limo >= 50 and (arcilla >= 12 and arcilla < 27)) or ((limo >= 50 and limo < 80) and arcilla < 12)):
        tipo = "franco limoso"
    elif (limo >= 80 and arcilla < 12):
        tipo = "limoso"
    elif ((arcilla >= 20 and arcilla < 35) and (limo < 28) and (arena > 45)):
        tipo = "franco arcilloso areno9so"
    elif ((arcilla >= 27 and arcilla < 40) and (arena > 20 and arena <= 45)):
        tipo = "franco arecilloso"
    elif ((arcilla >= 27 and arcilla < 40) and (arena <= 20)):
        tipo = "franco arcilloso limoso"
    elif (arcilla >= 35 and arena > 45):
        tipo = "arcilloso arenoso"
    elif (arcilla >= 40 and limo >= 40):
        tipo = "arcilloso limoso"
    elif (arcilla >= 40 and arena <= 45 and limo < 40):
        tipo = "arcilloso"
    else:
        tipo = "no aplica"
    return jsonify(tipo)


if __name__ == '__main__':
    app.run(debug=True)
