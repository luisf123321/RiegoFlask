from . import prediction
from flask import request, jsonify
from werkzeug.utils import secure_filename
import os
from .predict import predict
@prediction.route("/upload", methods=['POST'])
def uploader():
    if request.method == 'POST':
        print("prediction")
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        print(filename)
        # Guardamos el archivo en el directorio "Archivos PDF"
        #f.save(os.path.join("app\\prediccion\\img\\", filename))  
        f.save(os.path.join("app/prediccion/img/", filename))        
        # Retornamos una respuesta satisfactoria
        #result = predict( os.path.join("app\\prediccion\\img\\", filename))
        result = predict( os.path.join("app/prediccion/img/", filename))
        return jsonify(result)