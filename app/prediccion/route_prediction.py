from . import prediction
from flask import request, jsonify
from werkzeug.utils import secure_filename
import os
from .predict import predict


import skimage.io
import base64
import io
import numpy as np
import matplotlib.pyplot as plt
from .suelo_10 import SoilClassifier

@prediction.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        json_data = request.json
        filename = json_data["filename"]
        image_base64 = json_data["image"]
        #print(image_base64)
        
        base64_img = image_base64[22:]
        #print(base64_img)
        base64_img_bytes = base64_img.encode('utf-8')
        image_np = decode(base64_img_bytes)
        #plt.imshow(image_np)
        #plt.show()
        
        
        soil_classifier = SoilClassifier()
        # soil_class = soil_classifier.get_soil_class(image_filename)
        soil_class = soil_classifier.get_soil_class_np(image_np)
        print(type(soil_class))
        print(soil_class)    
        return jsonify(soil_class)


def decode(base64_string):
    if isinstance(base64_string, bytes):
        base64_string = base64_string.decode("utf-8")
    imgdata = base64.b64decode(base64_string)
    img = skimage.io.imread(imgdata, plugin='imageio')
    return img
