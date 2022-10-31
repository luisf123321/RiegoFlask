from contextlib import nullcontext
from app.dao.sectores_dao import SectoresDao
from app.models.sectores import Sector

import json


class SectoresLogica:
    @classmethod
    def obtenerSectoresByLotes(cls, lote):
        sectores = SectoresDao.seleccionarByLotes(lote=lote)
        if sectores is None:
            return dict({"code": 400, "message": "Sectores no encontrado"})
        else:            
            sectores_result = []
            for sector in sectores:
                sector = json.dumps(sector.__dict__)
                sector = sector.replace("_", "")
                sectores_result.append(json.loads(sector))
            return dict({"code": 200, "message": "sectores encontrados", "sectores": sectores_result})
    

    @classmethod
    def obtenerSectoresByCultivo(cls, cultivo):
        sectores = SectoresDao.seleccionarByCultivo(cultivo=cultivo)
        if sectores is None:
            return dict({"code": 400, "message": "Sectores no encontrado"})
        else:            
            sectores_result = []
            for sector in sectores:
                sector = json.dumps(sector.__dict__)
                sector = sector.replace("_", "")
                sectores_result.append(json.loads(sector))
            return dict({"code": 200, "message": "sectores encontrados", "sectores": sectores_result})
