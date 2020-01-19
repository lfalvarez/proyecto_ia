import unittest
from base import Record, Ruta, ManagerDeRutas, valida


class TestCases(unittest.TestCase):
    def setUp(self):
        self.r1 = Record("0", "CAL", "2", "2019-06-19 16:06:18.941", "2019-06-19 16:10:18.141", "S2", "5")
        self.r2 = Record("1", "S2", "1", "2019-06-19 16:17:24.550", "2019-06-19 16:29:10.882", "S1", "2")
        self.r3 = Record("3", "S1", "2", "2019-06-19 16:31:24.550", "2019-06-19 16:33:10.882", "S2", "1")

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
        por_donde_debe_pasar = ['CAL', 'S2', 'S1', 'S2']  ## Esto representa los nodos por donde debe pasar
        ## También es más o menos la ruta r1, r2 y r3
        ruta1 = Ruta([self.r1, self.r2, self.r3])
        self.assertTrue(ruta1.pasa_por(por_donde_debe_pasar))

    def test_ruta_invalida(self):
        por_donde_deberia_pasar = ['CAL', 'S2', 'S1', 'S3']  ## Esto representa los nodos por donde debe pasar
        ## Esta ruta no es la misma que está ahí reflejada por las rutas r1, r2, r3
        ruta = Ruta([self.r1, self.r2, self.r3])
        self.assertFalse(ruta.pasa_por(por_donde_deberia_pasar))

    def test_manager_de_rutas(self):
        manager = ManagerDeRutas()
        manager.leer_registros()
        self.assertGreater(len(manager.records), 10)  ## Hay más de 10 filas
        ruta = manager.obtenerRuta(['1', '4', '5', '7'])
        self.assertIsInstance(ruta, Ruta)
        self.assertEqual(len(ruta.records), 4)  ## Hay 4 registros del excel aquí

    def test_ruta_de_2(self):
        records = [Record("33", "SCL", "1", "2019-06-19 21:36:29.906000", "2019-06-19 21:46:39.994000" , "S1", "3"),
                   Record("35", "S1", "2", "2019-06-19 21:49:24.291000", "2019-06-19 22:01:10.613000" , "S2", "1"),
                   Record("39", "S2", "1", "2019-06-19 22:36:47.065000", "2019-06-19 22:48:33.412000" , "S1", "2"),
                   Record("43", "S1", "2", "2019-06-19 23:09:02.921000", "2019-06-19 23:20:41.941000" , "SCL", "3")]

        ruta = Ruta(records)
        self.assertTrue(ruta.pasa_por(['SCL', 'S1', 'S2', 'S1', 'SCL']))

    def test_ruta_de_3(self):
        records = [Record("33", "S1", "1", "2019-06-19 21:36:29.906000", "2019-06-19 21:46:39.994000" , "SCL", "3"),
                   Record("34", "S2", "2", "2019-06-19 21:38:28.011000", "2019-06-19 21:44:48.755000" , "SCL", "3"),
                   Record("35", "S2", "2", "2019-06-19 21:49:24.291000", "2019-06-19 22:01:10.613000" , "S1", "1"),
                   Record("39", "S1", "1", "2019-06-19 22:36:47.065000", "2019-06-19 22:48:33.412000" , "S2", "2"),
                   Record("43", "S2", "2", "2019-06-19 23:09:02.921000", "2019-06-19 23:20:41.941000" , "SCL", "3")]

        ruta = Ruta(records)
        self.assertFalse(ruta.pasa_por(['SCL', 'S1', 'SCL', 'S3', 'S1']))

    def test_ruta_de_4(self):
        records = [Record("33", "S1", "1", "2019-06-19 21:36:29.906000", "2019-06-19 21:46:39.994000" , "SCL", "3"),
                   Record("63", "S2", "2", "2019-06-20 02:01:31.762000", "2019-06-20 02:11:31.676000" , "CAL", "5")]

        ruta = Ruta(records)
        self.assertFalse(ruta.pasa_por( ['SCL', 'S1', 'S2']))

    def test_ruta_de_5(self):
        records = [Record("33", "S1", "1", "2019-06-19 21:36:29.906000", "2019-06-19 21:46:39.994000" , "SCL", "3"),
                   Record("63", "S1", "2", "2019-06-20 02:01:31.762000", "2019-06-20 02:11:31.676000" , "CAL", "5")]

        ruta = Ruta(records)
        self.assertFalse(ruta.pasa_por( ['SCL', 'S1', 'S2']))

    def test_ruta_de_6(self):
        records = [Record("33", "S1", "1", "2019-06-19 21:36:29.906000", "2019-06-19 21:46:39.994000" , "SCL", "3"),
                   Record("62", "S1", "1", "2019-06-20 02:01:19.488000", "2019-06-20 02:12:51.201000" , "CAL", "5"),
                   Record("63", "CAL", "2", "2019-06-20 02:01:31.762000", "2019-06-20 02:11:31.676000" , "S2", "5")]

        ruta = Ruta(records)
        self.assertFalse(ruta.pasa_por(['SCL', 'S1', 'S2', 'CAL']))

    def test_asegurar_orden_cronologico_true(self):
        records = [Record("33", "S1", "1", "2019-06-19 21:36:29.906000", "2019-06-19 21:46:39.994000" , "SCL", "3"),
                   Record("62", "S1", "1", "2019-06-20 02:01:19.488000", "2019-06-20 02:12:51.201000" , "S2", "5"),
                   Record("63", "S2", "2", "2019-06-20 02:01:31.762000", "2019-06-20 02:11:31.676000" , "CAL", "5")]

        ruta = Ruta(records)
        self.assertTrue(ruta.asegurar_orden_cronologico())

    def test_asegurar_orden_cronologico_false(self):
        records = [Record("33", "S1", "1", "2019-06-21 21:36:29.906000", "2019-06-19 21:46:39.994000" , "SCL", "3"),
                   Record("62", "S1", "1", "2019-06-20 02:01:19.488000", "2019-06-20 02:12:51.201000" , "S2", "5"),
                   Record("63", "S2", "2", "2019-06-20 02:01:31.762000", "2019-06-20 02:11:31.676000" , "CAL", "5")]

        ruta = Ruta(records)
        self.assertFalse(ruta.asegurar_orden_cronologico())

    def test_valida_orden(self):
        orden_malo = ['S1', 'SCL', 'S1', 'CAL', 'S1', 'S2', 'S2', 'CAL']
        query = ['SCL', 'S1', 'S2', 'CAL']
        self.assertFalse(valida(query, orden_malo))

    def test_valida_orden2(self):
        orden_bueno = ['S1', 'S2', 'S2', 'CAL', 'CAL', 'S3']
        query = ['S1', 'S2', 'CAL','S3']
        self.assertTrue(valida(query, orden_bueno))

    def test_valida_orden3(self):
        orden_malo = ['SCL', 'S2', 'S2', 'SCL', 'S2', 'CAL']
        query = ['SCL', 'S2', 'CAL']
        self.assertFalse(valida(query, orden_malo))

if __name__ == '__main__':
    unittest.main()
