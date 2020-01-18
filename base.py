import csv
import datetime
from collections import OrderedDict


class Record:
    def __init__(self,
                 access_id,
                 start_node_str,
                 start_node_id,
                 start_time,
                 stop_time,
                 end_node_str,
                 end_node_id):
        self.access_id = access_id
        self.start_node_str = start_node_str
        self.start_node_id = start_node_id
        self.end_node_str = end_node_str
        self.end_node_id = end_node_id
        self.start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S.%f')
        self.stop_time = datetime.datetime.strptime(stop_time, '%Y-%m-%d %H:%M:%S.%f')

    def __repr__(self):
        representation = '{access_id}, {start_node_str}, {start_node_id}, {end_node_str}, {end_node_id}, {start_time}, {stop_time}'
        return representation.format(access_id=self.access_id,
                                     start_node_str=self.start_node_str,
                                     start_node_id=self.start_node_id,
                                     end_node_str=self.end_node_str,
                                     end_node_id=self.end_node_id,
                                     start_time=self.start_time,
                                     stop_time=self.stop_time)


class Ruta:
    def __init__(self):
        self.records = []

    def append(self, ruta):
        self.records.append(ruta)

    def se_demora(self):
        primera_ruta = self.records[0]
        ultima_ruta = self.records[-1]
        diff = ultima_ruta.start_time - primera_ruta.start_time
        return diff

    def valida_que_nodo_sigue_en_ruta(self, index, nodos_actuales, nodo_a_comprobar):
        min = index - 1 if (index - 1) >= 0 else index
        max = index + 1 if (index) < len(nodos_actuales) else index
        subset_de_nodos = nodos_actuales[min:max + 1]
        if nodo_a_comprobar not in subset_de_nodos:
            return False
        return True

    def pasa_por(self, nodos):
        nodos_actuales = []
        for nodo in self.records:
            nodos_actuales.append(nodo.start_node_str)
            nodos_actuales.append(nodo.end_node_str)
        for index, nodo in enumerate(nodos):
            if not self.valida_que_nodo_sigue_en_ruta(index, nodos_actuales, nodo):
                return False
        ## Esto es para el último salto que no está incluido dentro del loop
        return self.valida_que_nodo_sigue_en_ruta(index, nodos_actuales, nodo)



class ManagerDeRutas:
    def __init__(self):
        self.records = []

    def leer_registros(self):
        records = []
        with open('access.csv') as access:
            reader = csv.DictReader(access, delimiter=',')
            for row in reader:
                access_id = row['access']
                start_node_str = row['from']
                start_node_id = row['from_i']
                start_time = row['start_time']
                stop_time = row['stop_time']
                end_node_str = row['to']
                end_node_id = row['to_i']
                r = Record(access_id,
                           start_node_str,
                           start_node_id,
                           start_time,
                           stop_time,
                           end_node_str,
                           end_node_id)
                records.append(r)
        self.records = records
        return self.records

    def obtenerRuta(self, indices_en_el_excel):
        registros = []
        for indice in indices_en_el_excel:
            indice = int(indice)
            registros.append(self.records[indice])

        ruta_resultante = Ruta()
        ruta_resultante.records = registros
        return ruta_resultante

if __name__ == '__main__':
    registros = ManagerDeRutas().leer_registros()
    print(registros[192])
    print(registros[196])
