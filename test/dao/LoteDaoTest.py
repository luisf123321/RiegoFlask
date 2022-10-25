import unittest
import sys
sys.path.append("C:\\Users\\LUISFERNANDO\\Documents\\proyecto-code\\RiegoFlask\\app\\dao")

from lotes_dao import LotesDao
sys.path.append("C:\\Users\\LUISFERNANDO\\Documents\\proyecto-code\\RiegoFlask\\app\\models")
from lote import Lote

class LoteDaoTest(unittest.TestCase):
    def test_get_lotess(self):
        self.assertIsNotNone(LotesDao.seleccionarTodos())
    def test_get_lotes_by_finca(self):
        lote = Lote(finca=1)
        self.assertIsNotNone(LotesDao.buscarPorFinca(lote))    
    def test_get_lote_by_id(self):
        lote = Lote(id=2)
        self.assertIsNotNone(LotesDao.buscarPorId(lote))
    def test_get_lote_by_id_not_valid(self):
        lote = Lote(id=15)
        self.assertIsNone(LotesDao.buscarPorId(lote))
    def test_delete_lote_by_id(self):
        lote = Lote(id=7)
        self.assertEqual(LotesDao.eliminar(lote),1)
    def test_insert_lote(self):
        lote = Lote(nombre="lot-07", area=12,
                          latitud=2.883137459182263, longitud=-75.26639088403925, altitud=0, finca=1)
        self.assertEqual(LotesDao.insertar(lote),1)
    def test_actualizar_lote(self):
        lote = Lote(nombre="lot-07", area=12,
                          latitud=2.883137459182263, longitud=-75.26639088403925, altitud=0, finca=1, id=6)
        self.assertEqual(LotesDao.actualizar(lote),1)


if __name__ == '__main__':
    unittest.main()