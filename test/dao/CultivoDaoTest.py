import unittest
import sys
sys.path.append("C:\\Users\\LUISFERNANDO\\Documents\\proyecto-code\\RiegoFlask\\app\\dao")

from cultivo_dao import CultivoDao
sys.path.append("C:\\Users\\LUISFERNANDO\\Documents\\proyecto-code\\RiegoFlask\\app\\models")
from cultivo import Cultivo

class CultivoDaoTest(unittest.TestCase):
    def test_get_cultivos(self):
        self.assertIsNotNone(CultivoDao.seleccionarTodos())
    def test_get_cultivos_by_user(self):
        cultivo = Cultivo(user=25)
        self.assertIsNotNone(CultivoDao.buscarPorUsuario(cultivo))    
    def test_get_cultivo_by_id(self):
        cultivo = Cultivo(id=2)
        self.assertIsNotNone(CultivoDao.buscarPorId(cultivo))
    def test_get_cultivo_by_id_not_valid(self):
        cultivo = Cultivo(id=3)
        self.assertIsNone(CultivoDao.buscarPorId(cultivo))
    def test_delete_cultivo_by_id(self):
        cultivo = Cultivo(id=29)
        self.assertEqual(CultivoDao.eliminar(cultivo),1)
    def test_insert_cultivo(self):
        cultivo = Cultivo(cultivoNombre="manzana", tipoCultivo=1,
                          fechaInicio="2022-01-01", fechaFinal="2023-01-01", cultivoEstado=1, user=25)
        self.assertEqual(CultivoDao.insertar(cultivo),1)
    def test_actualizar_cultivo(self):
        cultivo = Cultivo(cultivoNombre="manzana", tipoCultivo=1,
                          fechaInicio="2022-01-01", fechaFinal="2023-01-01", cultivoEstado=1, user=25,id=26)
        self.assertEqual(CultivoDao.actualizar(cultivo),1)
if __name__ == '__main__':
    unittest.main()