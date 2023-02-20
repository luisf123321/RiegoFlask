from flask import Flask, request, jsonify
from flask_cors import CORS
from app import create_app

app = create_app()

CORS(app)


@app.route('/')
def hello_world():
    return jsonify("hello world blanca")


if __name__ == '__main__':
    app.run(debug=True)
