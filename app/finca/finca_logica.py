from app.models.finca import Finca
from app.dao.finca_dao import FincaDao
import json


class FincaLogica:
    @classmethod
    def crearFinca(cls, data):
        nombre = data.get("nombre", None)
        direccion = data.get("direccion", None)
        latitud = data.get("latitud", None)
        longitud = data.get("longitud", None)
        altitud = data.get("altitud", None)
        user_id = data.get("user_is", None)
        finca = Finca(nombre=nombre, direccion=direccion, latitud=latitud,
                      longitud=longitud, altitud=altitud, usuario=user_id)
        rows = FincaDao.insertar(finca)
        if rows is not None:
            finca = json.dumps(finca.__dict__)
            finca = finca.replace("_", "")
            return dict({"code": 200, "message": "Finca creada", "finca": json.loads(finca)})
        else:
            return dict({"code": 400, "message": "Finca no se creo"})

    @classmethod
    def actualizarFinca(cls, data, idfinca):
        finca = Finca(id=idfinca)
        finca = FincaDao.buscarFincaPorId(finca)
        if finca is None:
            return dict({"code": 400, "message": "Finca no encontrado"})
        else:
            nombre = data.get("nombre", None)
            direccion = data.get("direccion", None)
            latitud = data.get("latitud", None)
            longitud = data.get("longitud", None)
            altitud = data.get("altitud", None)
            user_id = data.get("user_is", None)
            finca = Finca(nombre=nombre, direccion=direccion, latitud=latitud,
                        longitud=longitud, altitud=altitud, usuario=user_id, id=idfinca)
            rows = FincaDao.actualizar(finca)
            if rows is not None:
                finca = json.dumps(finca.__dict__)
                finca = finca.replace("_", "")
                return dict({"code": 200, "message": "Finca actializada", "finca": json.loads(finca)})
            else:
                return dict({"code": 400, "message": "Finca sin cambios"})

    @classmethod
    def buscarPorId(cls, idFinca):
        finca = Finca(id=idFinca)
        finca = FincaDao.buscarFincaPorId(finca)
        if finca is None:
            return dict({"code": 400, "message": "Finca no encontrado"})
        else:
            finca = json.dumps(finca.__dict__)
            finca = finca.replace("_", "")
            return dict({"code": 200, "message": "Finca encontrado", "finca": json.loads(finca)})

    @classmethod
    def buscarPorUsuario(cls, usuario_id):
        finca = Finca(usuario=usuario_id)
        fincas = FincaDao.buscarFincaPorUsuario(finca)
        if fincas is None:
            return dict({"code": 400, "message": "Finca no encontrado"})
        else:
            print("*"*20)
            print(fincas)
            fincas_result = []
            for finca in fincas:
                finca = json.dumps(finca.__dict__)
                finca = finca.replace("_", "")
                fincas_result.append(json.loads(finca))
            return dict({"code": 200, "message": "Fincas encontradas", "fincas": fincas_result})
