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

    @classmethod
    def obtenerSectoresByUsuario(cls, usuario):
        sectores = SectoresDao.seleccionarByUsuario(usuario=usuario)
        if sectores is None:
            return dict({"code": 400, "message": "Sectores no encontrado"})
        else:
            sectores_result = []
            for sector in sectores:
                sector = json.dumps(sector.__dict__)
                sector = sector.replace("_", "")
                sector = json.loads(sector)
                sector['value'] = sector['id']
                sector['label'] = sector['nombre']
                sectores_result.append(sector)
            return dict({"code": 200, "message": "sectores encontrados", "sectores": sectores_result})

    @classmethod
    def crearSector(cls, data):
        nombre = data.get("nombre", None)
        lat = data.get("latitud", None)
        long = data.get("longitud", None)
        area = data.get("area", None)
        lote_id = data.get("lote", None)
        cultivo = data.get("cultivo", None)
        tipo_suelo = data.get("tipoSuelo", None)
        altitud = data.get("altitud", None)
        nodo = data.get("nodo", None)
        sector = Sector(altitud=altitud, longitud=long,
                        latitud=lat, area=area, cultivo=cultivo,
                        lote=lote_id, nodo=nodo, nombre=nombre, suelo=tipo_suelo)
        print("secotr", sector.altitud)
        print("secotr", sector.longitud)
        print("secotr", sector.latitud)
        print("secotr", sector.area)
        print("secotr", sector.cultivo)
        print("secotr", sector.lote)
        print("secotr", sector.nodo)
        print("secotr", sector.nombre)
        print("secotr", sector.suelo)
        result = SectoresDao.insertar(sector=sector)
        if result is not None:
            sector = json.dumps(sector.__dict__)
            sector = sector.replace("_", "")
            return dict({"code": 200, "message": "Sector creado", "sector": json.loads(sector)})
        else:
            return dict({"code": 400, "message": "No se creo sector"})
