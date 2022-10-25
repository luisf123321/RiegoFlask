import unittest
import sys
sys.path.append("C:\\Users\\LUISFERNANDO\\Documents\\proyecto-code\\RiegoFlask\\app\\dao")

from finca_dao import FincaDao
sys.path.append("C:\\Users\\LUISFERNANDO\\Documents\\proyecto-code\\RiegoFlask\\app\\models")
from finca import Finca

class FincaDaoTest(unittest.TestCase):
    def test_get_fincas(self):
        self.assertIsNotNone(FincaDao.seleccionarTodos())
    def test_get_finca_by_user(self):
        finca = Finca(usuario=25)
        self.assertIsNotNone(FincaDao.buscarFincaPorUsuario(finca))    
    def test_get_finca_by_id(self):
        finca = Finca(id=2)
        self.assertIsNotNone(FincaDao.buscarFincaPorId(finca))
    def test_get_finca_by_id_not_valid(self):
        finca = Finca(id=90)
        self.assertIsNone(FincaDao.buscarFincaPorId(finca))
    def test_delete_finca_by_id(self):
        finca = Finca(id=11)
        self.assertEqual(FincaDao.eliminar(finca),1)
    def test_insert_finca(self):
        finca = Finca(nombre="eden 2", direccion="cr 31 sur ",
                          latitud=2.883137459182263, longitud=-75.26639088403925, altitud=0, usuario=25)
        self.assertEqual(FincaDao.insertar(finca),1)
    def test_actualizar_finca(self):
        finca = Finca(nombre="eden 2", direccion="cr 31 sur ",
                          latitud=2.883137459182263, longitud=-75.26639088403925, altitud=0, usuario=25, id=4)
        self.assertEqual(FincaDao.actualizar(finca),1)


if __name__ == '__main__':
    unittest.main()