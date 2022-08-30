from app.models.lote import Lote
from app.dao.lotes_dao import LotesDao
import json


class LoteLogica:
    @classmethod
    def buscarPorFinca(cls,finca_id):
        lote = Lote(finca=finca_id)
        lotes = LotesDao.buscarPorFinca(lote)
        if lotes is None:
            return dict({"code": 400, "message": "Lotes no encontrado"})
        else:
            print("*"*20)
            print(lotes)
            lotes_result = []
            for lote in lotes:
                lote = json.dumps(lote.__dict__)
                lote = lote.replace("_","")
                lotes_result.append(json.loads(lote))
            return dict({"code": 200, "message": "Cultivo encontrado", "lotes": lotes_result})
    @classmethod
    def buscarPorId(cls,id):
        lote = Lote(id=id)
        lote = LotesDao.buscarPorId(lote)
        if lote is None:
            return dict({"code": 400, "message": "Lotes no encontrado"})
        else:
            lote = lote.replace("_","")
            return dict({"code": 200, "message": "Cultivo encontrado", "lote": lote})  
    
    @classmethod
    def crear(cls, data):
        nombre = data.get("nombre", None)
        area = data.get("area", None)
        latitud = data.get("latitud", None)
        longitud = data.get("longitud", None)
        altitud = data.get("altitud", None)
        finca_id = data.get("finca_id", None)
        finca = Lote(nombre=nombre,area=area,latitud=latitud,longitud=longitud,altitud=altitud,finca=finca_id)
        rows = LotesDao.insertar(finca)
        if rows is None:
            return dict({"code": 400, "message": "No se creo lote"})
        else:
            finca = json.dumps(finca.__dict__)
            finca = finca.replace("_", "")
            return dict({"code": 200, "message": "Lote creado", "cultivo": json.loads(finca)})
        
    @classmethod
    def actualizar(cls, data, idLote):
        lote = Lote(id=idLote)
        lote = LotesDao.buscarPorId(lote)
        if lote is None:
            return dict({"code": 400, "message": "Lotes no encontrado"})
        else:
            nombre = data.get("nombre", None)
            area = data.get("area", None)
            latitud = data.get("latitud", None)
            longitud = data.get("longitud", None)
            altitud = data.get("altitud", None)
            finca_id = data.get("finca_id", None)
            finca = Lote(nombre=nombre,area=area,latitud=latitud,longitud=longitud,altitud=altitud,finca=finca_id)
            rows = LotesDao.insertar(finca)
            if rows is None:
                return dict({"code": 400, "message": "No se creo lote"})
            else:
                finca = json.dumps(finca.__dict__)
                finca = finca.replace("_", "")
                return dict({"code": 200, "message": "Lote creado", "cultivo": json.loads(finca)})

