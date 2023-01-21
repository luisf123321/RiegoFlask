from app.dao.tipo_riego_dao import TipoRiegoDao
from app.dao.admin_riego_dao import AdminRiegoDao
import json

from app.models.admin_riego import AdminRiego
from app.models.tipo_riego import TipoRiego
from app.dao.tipo_dispositivo_dao import TipoDispositivoDao
from app.dao.dispositivo_dao import DispositivoDao
from app.models.dispositivo import Dispositivo


from app.dao.tipo_riego_dao import TipoRiegoDao


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
                tipoRiego = tipoRiego.replace("_", "")
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
                riego = riego.replace("_", "")
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
                tipodispositivo = tipodispositivo.replace("_", "")
                tipodispositivo = json.loads(tipodispositivo)
                tipodispositivo['value'] = tipodispositivo['id']
                tipodispositivo['label'] = tipodispositivo['categoria']
                tipos_dispositivos_result.append(tipodispositivo)
            return dict({"code": 200, "message": "tipos dispositivos encontrados", "tipos": tipos_dispositivos_result})

    @classmethod
    def crearDispositivo(cls, data):
        nombre = data.get("nombre", None)
        descripcion = data.get("descripcion", None)
        tipoDispositivo = data.get("tipoDispositivo", None)
        tipoSector = data.get("tipoSector", None)
        dispositivo = Dispositivo(disEstado=1, disModelo=descripcion,
                                  disNombre=nombre, disSectores=tipoSector, disTipo=tipoDispositivo)
        rows = DispositivoDao.insertar(dispositivo)
        if rows is not None:
            dispositivo = json.dumps(dispositivo.__dict__)
            dispositivo = dispositivo.replace("_", "")
            return dict({"code": 200, "message": "Dispositivo creada", "dispositivo": json.loads(dispositivo)})
        else:
            return dict({"code": 400, "message": "Dispositivo no se creo"})

    @classmethod
    def crearAdminRiego(cls, data):
        caudal = data.get("caudal", None)
        distancia = data.get("distancia", None)
        radio = data.get("radio", None)
        tipoRiego = data.get("tipoRiego", None)
        tipo_riego = TipoRiegoDao.seleccionarById(id=tipoRiego)
        tipoSector = data.get("tipoSector", None)
        admin = AdminRiego(caudal=caudal, distancia=distancia, efectividad=tipo_riego.efectividad,
                           nad=65, radio=radio, tipoRiego=tipoRiego, sector=tipoSector)
        rows = AdminRiegoDao.insertar(adminRiego=admin)
        if rows is not None:
            admin = json.dumps(admin.__dict__)
            admin = admin.replace("_", "")
            return dict({"code": 200, "message": "Riego creada", "riego": json.loads(admin)})
        else:
            return dict({"code": 400, "message": "Riego no se creo"})

    @classmethod
    def obtenerDispositivoByUsuario(cls, userId):
        registros = DispositivoDao.seleccionarByUsuario(usuario=userId)
        if registros is None:
            return dict({"code": 400, "message": "los dispositivos no encontraron"})
        else:
            print("*"*20)
            print(registros)
            dispositivos_result = []
            for dispositivos in registros:
                dispositivos = json.dumps(dispositivos.__dict__)
                dispositivos = dispositivos.replace("_", "")
                dispositivos = json.loads(dispositivos)
                dispositivos_result.append(dispositivos)
            return dict({"code": 200, "message": "dispositivos encontrados", "dispositivos": dispositivos_result})

    @classmethod
    def obtenerDispositivoBysectore(cls, sector):
        registros = DispositivoDao.seleccionarBySectores(sector=sector)
        if registros is None:
            return dict({"code": 400, "message": "los dispositivos no encontraron"})
        else:
            print("*"*20)
            print(registros)
            dispositivos_result = []
            for dispositivos in registros:
                dispositivos = json.dumps(dispositivos.__dict__)
                dispositivos = dispositivos.replace("_", "")
                dispositivos = json.loads(dispositivos)
                dispositivos_result.append(dispositivos)
            return dict({"code": 200, "message": "dispositivos encontrados", "dispositivos": dispositivos_result})

    @classmethod
    def obtenerAdminRiegoByUsuario(cls, usuario):
        registros = AdminRiegoDao.buscarByUsuario(usuario=usuario)
        if registros is None:
            return dict({"code": 400, "message": "los riegos no encontraron"})
        else:
            print("*"*20)
            print(registros)
            admin_riego_result = []
            for adminriego in registros:
                adminriego = adminriego.replace("_", "")
                adminriego = json.loads(adminriego)
                admin_riego_result.append(adminriego)
            return dict({"code": 200, "message": "riegos encontrados", "riegos": admin_riego_result})
