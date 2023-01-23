from app.models.cultivo import Cultivo
from app.dao.cultivo_dao import CultivoDao
from app.dao.tipo_cultivo_dao import TipoCultivoDao
from app.models.tipo_cultivo import TipoCultivo
import json
from app.email.body import BodyEmail
from app.email.send import SendEmail
from datetime import date, timedelta, datetime
import maya


class CultivoLogica:
    @classmethod
    def eliminarCultivo(cls, id):
        cultivo = Cultivo(id=id)
        cultivo = CultivoDao.buscarPorId(cultivo=cultivo)
        if cultivo is None:
            return dict({"code": 400, "message": "Cultivo no encontrado"})
        result = CultivoDao.eliminar(cultivo=cultivo)
        if result >= 1:
            cultivo = json.dumps(cultivo.__dict__)
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
            fecha_siembra = cultivo.fechaSiembra
            fecha_inicio = cultivo.fechaInicio
            fecha_fin = cultivo.fechaFinal
            fecha_desarrollo = cultivo.fechaDesarrollo
            fecha_maduracion = cultivo.fechaMaduracion

            dias_inicio = (fecha_inicio - fecha_siembra).days
            dias_desarrollo = (fecha_desarrollo - fecha_inicio).days
            dias_maduracion = (fecha_maduracion - fecha_desarrollo).days
            dias_final = (fecha_fin - fecha_maduracion).days

            fecha_inicio = fecha_inicio.strftime('%Y-%m-%d')
            fecha_desarrollo = fecha_desarrollo.strftime('%Y-%m-%d')
            fecha_maduracion = fecha_maduracion.strftime('%Y-%m-%d')
            fecha_fin = fecha_fin.strftime('%Y-%m-%d')
            fecha_siembra = fecha_siembra.strftime('%Y-%m-%d')
            cultivo.fechaSiembra = fecha_siembra
            cultivo.fechaInicio = fecha_inicio
            cultivo.fechaFinal = fecha_fin
            cultivo.fechaDesarrollo = fecha_desarrollo
            cultivo.fechaMaduracion = fecha_maduracion

            cultivo = json.dumps(cultivo.__dict__)
            print(type(cultivo))
            cultivo = cultivo.replace("_", "")
            cultivo = json.loads(cultivo)
            cultivo['etapaInicia'] = dias_inicio
            cultivo['etapaDesarrollo'] = dias_desarrollo
            cultivo['etapaMaduracion'] = dias_maduracion
            cultivo['etapaFinal'] = dias_final
            return dict({"code": 200, "message": "Cultivo encontrado", "cultivo": cultivo})

    @classmethod
    def buscarCultivoPorUser(cls, idUser):
        cultivo = Cultivo(user=idUser)
        cultivos = CultivoDao.buscarPorUsuario(cultivo=cultivo)
        if cultivos is None:
            return dict({"code": 400, "message": "No hay cultivos   para el usuario"})
        else:
            cultivos_result = []
            for cultivo in cultivos:
                cultivo = json.dumps(cultivo.__dict__)
                cultivo = cultivo.replace("_", "")
                cultivo['value'] = cultivo['id']
                cultivo['label'] = cultivo['cultivoNombre']
                cultivos_result.append(json.loads(cultivo))
            return dict({"code": 200, "message": "Cultivo encontrado", "cultivo": cultivos_result})

    @classmethod
    def tipocultivos(cls):
        tipos = TipoCultivoDao.seleccionarTodos()
        if tipos is None:
            return dict({"code": 400, "message": "No hay tipos de cultivos para el usuario"})
        else:
            tipos_cultivos_result = []
            for tipo in tipos:
                tipo = json.dumps(tipo.__dict__)
                tipo = tipo.replace("_", "")
                print(type(tipo))
                tipo = json.loads(tipo)
                tipo['value'] = tipo['id']
                tipo['label'] = tipo['nombre'] + ' - ' + \
                    tipo['variedad'] + '-' + tipo['referencia']
                tipos_cultivos_result.append(tipo)
            return dict({"code": 200, "message": "Tipos cultivo encontrado", "tipos": tipos_cultivos_result})

    @classmethod
    def crearCultivo(cls, data):
        nombre = data.get("nombre", None)
        tipo_cultivo = data.get("tipoCultivo", None)

        tipoCultivo = TipoCultivoDao.buscarPorId(tipo_cultivo)
        fecha_siembra = data.get("fechaInicio", None)
        fecha_siembra = maya.parse(fecha_siembra).datetime()
        print("fecha siembra", fecha_siembra)
        fecha_final = data.get("fechaFinal", None)
        fecha_final = maya.parse(fecha_final).datetime()
        print("fecha final", fecha_final)
        fecha_inicio = fecha_siembra + timedelta(tipoCultivo.inicial)
        fecha_desarrollo = fecha_inicio + timedelta(tipoCultivo.desarrollo)
        fecha_maduracion = fecha_desarrollo + timedelta(tipoCultivo.maduracion)
        #fecha_desarrollo = data.get("fechaDesarollo", None)
        #fecha_maduracion = data.get("fechaMaduracion", None)
        #estado = data.get("estado", None)
        user_id = data.get("user_id", None)
        cultivo = Cultivo(cultivoNombre=nombre, tipoCultivo=tipo_cultivo,
                          fechaSiembra=fecha_siembra, fechaFinal=fecha_final,
                          cultivoEstado=1, user=user_id, fechaMaduracion=fecha_maduracion,
                          fechaDesarrollo=fecha_desarrollo, fechaInicio=fecha_inicio)
        result = CultivoDao.insertar(cultivo=cultivo)
        if result is not None:
            htmlCultivo = BodyEmail.bodyToCrearCultivo(cultivo=cultivo)
            html = BodyEmail.body(bodyTempleate=htmlCultivo)
            SendEmail.send(html, 'encisolf901@gmail.com',
                           "Welcome to riego application")
            cultivo.fechaSiembra = cultivo.fechaSiembra.strftime('%Y-%m-%d')
            cultivo.fechaInicio = cultivo.fechaInicio.strftime('%Y-%m-%d')
            cultivo.fechaDesarrollo = cultivo.fechaDesarrollo.strftime(
                '%Y-%m-%d')
            cultivo.fechaMaduracion = cultivo.fechaMaduracion.strftime(
                '%Y-%m-%d')
            cultivo.fechaFinal = cultivo.fechaFinal.strftime('%Y-%m-%d')
            cultivo = json.dumps(cultivo.__dict__)
            cultivo = cultivo.replace("_", "")
            return dict({"code": 200, "message": "Cultivo creado", "cultivo": json.loads(cultivo)})
        else:
            return dict({"code": 400, "message": "No se creo cultivo"})

    @classmethod
    def actualizarCultivo(cls, data, idCultivo):
        cultivo = Cultivo(id=idCultivo)
        cultivo = CultivoDao.buscarPorId(cultivo=cultivo)
        if cultivo is None:
            return dict({"code": 400, "message": "Cultivo no encontrado"})
        else:
            nombre = data.get("nombre", None)
            tipo_cultivo = data.get("tipoCultivo", None)
            fecha_inicio = data.get("fechaInicio", None)
            fecha_final = data.get("fechaFinal", None)
            fecha_desarrollo = data.get("fechaDesarollo", None)
            fecha_maduracion = data.get("fechaMaduracion", None)
            estado = data.get("estado", None)
            user_id = data.get("user_id", None)
            cultivo = Cultivo(cultivoNombre=nombre, tipoCultivo=tipo_cultivo, fechaInicio=fecha_inicio,
                              fechaFinal=fecha_final, cultivoEstado=estado,
                              user=user_id, id=idCultivo, fechaMaduracion=fecha_maduracion,
                              fechaDesarrollo=fecha_desarrollo)
            CultivoDao.actualizar(cultivo=cultivo)
            cultivo = json.dumps(cultivo.__dict__)
            cultivo = cultivo.replace("_", "")
            return dict({"code": 200, "message": "Cultivo actializado", "cultivo": json.loads(cultivo)})
