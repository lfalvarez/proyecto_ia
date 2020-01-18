import unittest
from base import Record, Ruta, ManagerDeRutas


class TestCases(unittest.TestCase):
    def setUp(self):
        self.r1 = Record("0", "S2", "2", "2019-06-19 16:06:18.941", "2019-06-19 16:10:18.141", "CAL", "5")
        self.r2 = Record("1", "S1", "1", "2019-06-19 16:17:24.550", "2019-06-19 16:29:10.882", "S2", "2")
        self.r3 = Record("3", "S2", "2", "2019-06-19 16:31:24.550", "2019-06-19 16:33:10.882", "S1", "1")


    def test_datetime_(self):
        self.assertEqual(self.r1.start_time.year, 2019)
        self.assertEqual(self.r1.start_time.hour, 16)
        self.assertEqual(self.r1.start_time.minute, 6)
        self.assertEqual(self.r1.start_time.second, 18)
        self.assertEqual(self.r1.start_time.microsecond, 941000)

        self.assertEqual(self.r1.stop_time.year, 2019)
        self.assertEqual(self.r1.stop_time.hour, 16)
        self.assertEqual(self.r1.stop_time.minute, 10)
        self.assertEqual(self.r1.stop_time.second, 18)
        self.assertEqual(self.r1.stop_time.microsecond, 141000)

    def test_crear_una_ruta(self):
        ruta = Ruta()
        ruta.append(self.r2)
        ruta.append(self.r3)
        demora = ruta.se_demora()
        self.assertEqual(demora.seconds, 14 * 60)

    def test_ruta_valida(self):
        por_donde_debe_pasar = ['CAL', 'S2', 'S1', 'S2'] ## Esto representa los nodos por donde debe pasar
        ## También es más o menos la ruta r1, r2 y r3
        ruta = Ruta()
        ruta.append(self.r1)
        ruta.append(self.r2)
        ruta.append(self.r3)
        self.assertTrue(ruta.pasa_por(por_donde_debe_pasar))

    def test_ruta_invalida(self):
        por_donde_deberia_pasar = ['CAL', 'S2', 'S1', 'S3'] ## Esto representa los nodos por donde debe pasar
        ## Esta ruta no es la misma que está ahí reflejada por las rutas r1, r2, r3
        ruta = Ruta()
        ruta.append(self.r1)
        ruta.append(self.r2)
        ruta.append(self.r3)
        self.assertFalse(ruta.pasa_por(por_donde_deberia_pasar))

    def test_manager_de_rutas(self):
        manager = ManagerDeRutas()
        manager.leer_registros()
        self.assertGreater(len(manager.records), 10) ## Hay más de 10 filas
        ruta = manager.obtenerRuta(['1', '4', '5', '7'])
        self.assertIsInstance(ruta, Ruta)
        self.assertEqual(len(ruta.records), 4) ## Hay 4 registros del excel aquí

if __name__ == '__main__':
    unittest.main()
