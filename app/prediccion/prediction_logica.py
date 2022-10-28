
from app.dao.muestra_suelo import MuestraSueloDao
import json
class PredictionLogica:
    @classmethod
    def obtenerMuestrasSuelo(cls, usuario):
        muestras = MuestraSueloDao.seleccionarByUser(usuario=usuario)
        if muestras is None:
            return dict({"code": 400, "message": "No se encontraron muestra de suelos"})
        else:
            muestra_result = []
            for muestra in muestras:
                muestra.fecha = muestra.fecha.strftime('%Y-%m-%d') 
                muestra = json.dumps(muestra.__dict__)
                muestra = muestra.replace("_", "")
                muestra_result.append(json.loads(muestra))
            return dict({"code": 200, "message": "Muestras encontradas", "muestras": muestra_result})
