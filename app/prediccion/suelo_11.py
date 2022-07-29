#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 15:46:40 2022

@author: juancastro
"""

from flask import Flask, request, jsonify
from flask_cors import CORS

from PIL import Image
import skimage.io
import base64
import io
import numpy as np
import matplotlib.pyplot as plt

from suelo_10 import SoilClassifier

app = Flask(__name__)
CORS(app)


def decode(base64_string):
    if isinstance(base64_string, bytes):
        base64_string = base64_string.decode("utf-8")

    imgdata = base64.b64decode(base64_string)
    img = skimage.io.imread(imgdata, plugin='imageio')
    return img


@app.route("/", methods=["POST"])
def starting_url():
    json_data = request.json
    filename = json_data["filename"]
    image_base64 = json_data["image"]
    
    base64_img = image_base64[23:]
    base64_img_bytes = base64_img.encode('utf-8')
    image_np = decode(base64_img_bytes)
    #plt.imshow(image_np)
    #plt.show()
    
    
    soil_classifier = SoilClassifier()
    # soil_class = soil_classifier.get_soil_class(image_filename)
    soil_class = soil_classifier.get_soil_class_np(image_np)
    print(type(soil_class))
    print(soil_class)
    
    # soil_class = "{'thresholds': {'arcilla_top': 25, 'limo_top': 34, 'arena_bottom': 448, 'arena_top': 148}}"
    # type(soil_class)
    
    # import json

    # #json string data
    # employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'

    # #check data type with type() method
    # print(type(employee_string))

    # #convert string to  object()
    # json_object = json.loads(soil_class)

    # #check new data type
    # print(type(json_object))

    # {'components': {'arcilla': 1.69, 'limo': 32.74, 'arena': 65.57}}
    # {'thresholds': {'arcilla_top': 25, 'limo_top': 34, 'arena_bottom': 448, 'arena_top': 148}}

    return jsonify(soil_class)


if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=8080)
    
    app.run(debug = True)
