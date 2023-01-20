from app.dao.tipo_riego_dao import TipoRiegoDao
from app.dao.admin_riego_dao import AdminRiegoDao
import json

from app.models.admin_riego import AdminRiego
from app.models.tipo_riego import TipoRiego
from app.dao.tipo_dispositivo_dao import TipoDispositivoDao
from app.models.tipo_dispositivo import TipoDispositivo
class Riegologica:
    @classmethod
    def obtenerTipoDeRiego(cls):
        registros = TipoRiegoDao.seleccionarTodos()
        if registros is None:
             return dict({"code": 400, "message": "tipos de riego no encontrado"})
        else:
            print("*"*20)
            print(registros)
            tipos_riego_result = []
            for tipoRiego in registros:
                tipoRiego = tipoRiego.replace("_","")
                tipoRiego = json.loads(tipoRiego)
                tipoRiego['value'] = tipoRiego['id']
                tipoRiego['label'] = tipoRiego['nombre']
                tipos_riego_result.append(tipoRiego)
            return dict({"code": 200, "message": "sectores encontrados", "tipos": tipos_riego_result})
    
    @classmethod
    def buscarPorSector(cls, sector):
        print(sector)
        admin = AdminRiego(sector=sector)
        riegos = AdminRiegoDao.buscarSector(admin)
        if riegos is None:
            return dict({"code": 400, "message": "tipos de riego no encontrado"})
        else:
            print("*"*20)
            print(riegos)
            admin_riegos_result = []
            for riego in riegos:
                riego = riego.replace("_","")
                admin_riegos_result.append(json.loads(riego))
            return dict({"code": 200, "message": "sectores encontrados", "riegos": admin_riegos_result})

    @classmethod
    def obtenerTipoDeDispositivo(cls):
        registros = TipoDispositivoDao.seleccionarTodos()
        if registros is None:
             return dict({"code": 400, "message": "tipos de dispositivos no encontrado"})
        else:
            print("*"*20)
            print(registros)
            tipos_dispositivos_result = []
            for tipodispositivo in registros:
                tipodispositivo = tipodispositivo.replace("_","")
                tipodispositivo = json.loads(tipodispositivo)
                tipodispositivo['value'] = tipodispositivo['id']
                tipodispositivo['label'] = tipodispositivo['categoria']
                tipos_dispositivos_result.append(tipodispositivo)
            return dict({"code": 200, "message": "sectores encontrados", "tipos": tipos_dispositivos_result})
    
