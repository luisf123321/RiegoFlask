
from app.dao.muestra_suelo import MuestraSueloDao
from app.dao.tipo_suelo_dao import TipoSueloDao
import json
from app.models.muestra_suelo import MuestraSuelo
from datetime import datetime


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
                muestra = json.loads(muestra)
                muestra['value'] = muestra['id']
                muestra['label'] = " # " + str(muestra['id']) + " arena: " + str(muestra['arena']) + \
                    " limo: " + str(muestra['limo']) + \
                    " arcilla: " + str(muestra['arcilla'])
                muestra_result.append(muestra)
            return dict({"code": 200, "message": "Muestras encontradas", "muestras": muestra_result})

    @classmethod
    def obtenerTipoSuelo(cls):
        tipoSuelos = TipoSueloDao.seleccionarTodos()
        if tipoSuelos is None:
            return dict({"code": 400, "message": "No se encontraron muestra de suelos"})
        else:
            tipo_suelos_result = []
            for tipo in tipoSuelos:

                tipo = json.dumps(tipo.__dict__)
                tipo = tipo.replace("_", "")
                tipo = json.loads(tipo)
                tipo['value'] = tipo['id']
                tipo['label'] = tipo['nombre']
                tipo_suelos_result.append(tipo)
            return dict({"code": 200, "message": "Muestras encontradas", "suelos": tipo_suelos_result})

    @classmethod
    def crearMuestra(cls, data):
        arena = data.get("arena", None)
        limo = data.get("limo", None)
        arcilla = data.get("arcilla", None)
        tipoSuelo = data.get("tipoSuelo", None)
        usuario = data.get("usuario", None)
        muestra = MuestraSuelo(arcilla=arcilla, arena=arena, limo=limo,
                               usuario=usuario, tipoSuelo=tipoSuelo, fecha=datetime.now())
        print("muestra", muestra)
        result = MuestraSueloDao.insertar(sector=sector)
        if result is not None:
            sector = json.dumps(sector.__dict__)
            sector = sector.replace("_", "")
            return dict({"code": 200, "message": "Sector creado", "sector": json.loads(sector)})
        else:
            return dict({"code": 400, "message": "No se creo sector"})
