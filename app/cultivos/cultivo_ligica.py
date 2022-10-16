from app.models.cultivo import Cultivo
from app.dao.cultivo_dao import CultivoDao
from app.dao.tipo_cultivo_dao import TipoCultivoDao
from app.models.tipo_cultivo import TipoCultivo
import json
from app.email.body import BodyEmail
from app.email.send import SendEmail


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
            cultivo = json.dumps(cultivo.__dict__)
            cultivo = cultivo.replace("_", "")
            return dict({"code": 200, "message": "Cultivo encontrado", "cultivo": json.loads(cultivo)})

    @classmethod
    def buscarCultivoPorUser(cls, idUser):
        cultivo = Cultivo(user=idUser)
        cultivos = CultivoDao.buscarPorUsuario(cultivo=cultivo)
        if cultivos is None:
            return dict({"code": 400, "message": "No hay cultivos para el usuario"})
        else:
            cultivos_result = []
            for cultivo in cultivos:
                cultivo = json.dumps(cultivo.__dict__)
                cultivo = cultivo.replace("_", "")
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
                tipos_cultivos_result.append(json.loads(tipo))
            return dict({"code": 200, "message": "Tipos cultivo encontrado", "tipos": tipos_cultivos_result})

    @classmethod
    def crearCultivo(cls, data):
        nombre = data.get("nombre", None)
        tipo_cultivo = data.get("tipoCultivo", None)
        fecha_inicio = data.get("fechaInicio", None)
        fecha_final = data.get("fechaFinal", None)
        estado = data.get("estado", None)
        user_id = data.get("user_id", None)
        cultivo = Cultivo(cultivoNombre=nombre, tipoCultivo=tipo_cultivo,
                          fechaInicio=fecha_inicio, fechaFinal=fecha_final, cultivoEstado=estado, user=user_id)
        result = CultivoDao.insertar(cultivo=cultivo)
        if result is not None:            
            htmlCultivo = BodyEmail.bodyToCrearCultivo(cultivo=cultivo)
            html = BodyEmail.body(bodyTempleate=htmlCultivo)
            SendEmail.send(html, 'encisolf901@gmail.com',
                           "Welcome to riego application")
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
            estado = data.get("estado", None)
            user_id = data.get("user_id", None)
            cultivo = Cultivo(cultivoNombre=nombre, tipoCultivo=tipo_cultivo, fechaInicio=fecha_inicio,
                              fechaFinal=fecha_final, cultivoEstado=estado, user=user_id, id=idCultivo)
            CultivoDao.actualizar(cultivo=cultivo)
            cultivo = json.dumps(cultivo.__dict__)
            cultivo = cultivo.replace("_", "")
            return dict({"code": 200, "message": "Cultivo actializado", "cultivo": json.loads(cultivo)})
