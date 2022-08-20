from app.models.cultivo import Cultivo
from app.dao.cultivo_dao import CultivoDao
from app.dao.tipo_cultivo_dao import TipoCultivoDao
from app.models.tipo_cultivo import TipoCultivo
import json

class CultivoLogica:
    @classmethod
    def eliminarCultivo(cls, id):
        cultivo = Cultivo(id=id)
        cultivo = CultivoDao.buscarPorId(cultivo=cultivo)
        if cultivo is None:
            return dict({"code": 400, "message": "Cultivo no encontrado"})
        result = CultivoDao.eliminar(cultivo=cultivo)
        if result >= 1:
            cultivo =  json.dumps(cultivo.__dict__)
            cultivo = cultivo.replace("_", "")
            return dict({"code": 200, "message": "Cultivo eliminado", "cultivo": json.loads(cultivo)})
        else:
            return dict({"code": 400, "message": "No se pudo eliminar Cultivo"})

    
    @classmethod
    def buscarCultivoPorId(cls, id):
        cultivo = Cultivo(id=id)
        cultivo = CultivoDao.buscarPorId(cultivo=cultivo)
        if cultivo is None:
            return dict({"code": 400, "message": "Cultivo no encontrado"})
        else:
            cultivo =  json.dumps(cultivo.__dict__)
            cultivo = cultivo.replace("_", "")
            return dict({"code": 200, "message": "Cultivo encontrado", "cultivo": json.loads(cultivo)})

