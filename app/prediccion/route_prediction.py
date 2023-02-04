from . import prediction
from flask import request, jsonify
from werkzeug.utils import secure_filename
from app.prediccion.prediction_logica import PredictionLogica
#import os
#from .predict import predict


import skimage.io
import base64
from .suelo_classifier import SoilClassifier


@prediction.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        json_data = request.json
        filename = json_data["filename"]
        image_base64 = json_data["image"]
        # print(image_base64)

        base64_img = image_base64[22:]
        # print(base64_img)
        base64_img_bytes = base64_img.encode('utf-8')
        image_np = decode(base64_img_bytes)
        # plt.imshow(image_np)
        # plt.show()

        soil_classifier = SoilClassifier()
        # soil_class = soil_classifier.get_soil_class(image_filename)
        soil_class = soil_classifier.get_soil_class_np(image_np)
        print(type(soil_class))
        print(soil_class)
        return jsonify(soil_class)


"""
opencv-python
tensorflow
scikit-image
ipython
matplotlib


@prediction.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        json_data = request.json
        filename = json_data["filename"]
        image_base64 = json_data["image"]
        #print(image_base64)
        
        #base64_img = image_base64[22:]
        #print(base64_img)
        #base64_img_bytes = base64_img.encode('utf-8')
        #image_np = decode(base64_img_bytes)
        #plt.imshow(image_np)
        #plt.show()
        
        
        #soil_classifier = SoilClassifier()
        # soil_class = soil_classifier.get_soil_class(image_filename)
        #soil_class = soil_classifier.get_soil_class_np(image_np)
        #print(type(soil_class))
        #print(soil_class)    
        return jsonify({'components': {'arcilla': 8.0, 'limo': 1.26, 'arena': 90.74}, 'thresholds': {'arcilla_top': 48.0, 'limo_top': 39.0, 'arena_bottom': 469.0, 'arena_top': 88.0}})
"""


def decode(base64_string):
    if isinstance(base64_string, bytes):
        base64_string = base64_string.decode("utf-8")
    imgdata = base64.b64decode(base64_string)
    img = skimage.io.imread(imgdata, plugin='imageio')
    return img


@prediction.route("/muestras/<usuario>", methods=['GET'])
def muestras(usuario):
    try:
        response = PredictionLogica.obtenerMuestrasSuelo(usuario=usuario)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


@prediction.route("/suelos", methods=['GET'])
def suelos():
    try:
        response = PredictionLogica.obtenerMuestrasSuelo()
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500


@prediction.route('/', methods=['POST'])
def crear():
    try:
        data = request.json
        response = PredictionLogica.crearMuestra(data=data)
        if response['code'] == 200:
            return jsonify(response), 200
        else:
            return jsonify(response), 400
    except Exception as ex:
        print(ex)
        return jsonify(dict({"code": 500, "message": "No se pudo realizar cambios, vuelva intentar"})), 500
