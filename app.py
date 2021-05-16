from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/riego2'
mongo = PyMongo(app)

db = mongo.db.users


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/users', methods = ['POST'])
def createUser():
    print(request.json)
    d = request.json
    id = db.insert(d)
    return jsonify(str(ObjectId(id)))


@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for user in db.find():
        users.append({
            "_id": str(ObjectId(user['_id'])),
            "nombre": user['nombre'],
            "apellido": user['apellido'],
            "edad": user["edad"]
        })
    print(users)

    return jsonify(users)


@app.route('/user/<id>',methods=['GET'])
def getUser(id):
    user = db.find_one({"_id": ObjectId(id)})
    return jsonify(
        {
            "nombre":user['nombre'],
            "apellido": user['apellido']
        }
    )


@app.route('/user/<id>',methods=['DELETE'])
def deleteUser(id):
    user = db.delete_one({"_id": ObjectId(id)})
    return jsonify(
        {
            "message":"ok"
        }
    )


@app.route('/user/<id>', methods=['PUT'])
def updateUser(id):
    user = db.update_one({"_id": ObjectId(id)}, {"$set": {
        "nombre": request.json['nombre'],
        "apellido":request.json['apellido'],
        "edad": request.json['edad']
    }})
    return jsonify(
        {
            "message": "update"
        }
    )


if __name__ == '__main__':
    app.run()
