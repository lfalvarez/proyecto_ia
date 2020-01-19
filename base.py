import csv
import datetime
from copy import copy


class Record:
    def __init__(self,
                 access_id,
                 start_node_str,
                 start_node_id,
                 start_time,
                 stop_time,
                 end_node_str,
                 end_node_id):
        self.access_id = int(access_id)
        self.start_node_str = start_node_str
        self.start_node_id = start_node_id
        self.end_node_str = end_node_str
        self.end_node_id = end_node_id
        self.start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S.%f')
        self.stop_time = datetime.datetime.strptime(stop_time, '%Y-%m-%d %H:%M:%S.%f')

    def __repr__(self):
        representation = 'Record("{access_id}", "{start_node_str}", "{start_node_id}", "{start_time}", "{stop_time}" , "{end_node_str}", "{end_node_id}")'
        return representation.format(access_id=self.access_id,
                                     start_node_str=self.start_node_str,
                                     start_node_id=self.start_node_id,
                                     end_node_str=self.end_node_str,
                                     end_node_id=self.end_node_id,
                                     start_time=self.start_time,
                                     stop_time=self.stop_time)

def valida(query, nodos_para_validar):
    nodos_para_validar = list(reversed(nodos_para_validar))
    query = list(reversed(query))
    index = 0
    for nodoq in query:
        if nodoq != nodos_para_validar[index]:
            return False
        else:
            if len(nodos_para_validar) == index + 1:
                continue
            if nodos_para_validar[index + 1] == nodoq:
                index += 1
        index += 1
    return nodos_para_validar[index:][0] == nodos_para_validar[-1]


class Ruta:
    def __init__(self, records=[]):
        self.records = records

    def append(self, ruta):
        self.records.append(ruta)

    def se_demora(self):
        primera_ruta = self.records[0]
        ultima_ruta = self.records[-1]
        diff = ultima_ruta.start_time - primera_ruta.start_time
        return diff

    def valida_que_nodo_sigue_en_ruta(self, index, nodos_actuales, nodo_a_comprobar, cantidad_de_nodos_par):
        es_impar = bool(index % 2)
        min = index - 1 if (index - 1) >= 0 else index
        max = index + 1 if (index) < len(nodos_actuales) or es_impar else index
        if es_impar:
            subset_1 = nodos_actuales[min:max]
            subset_2 = nodos_actuales[max: max+2]
            result = nodo_a_comprobar in subset_1 and nodo_a_comprobar in subset_2
            return result
        factor = 1 if index > 0 else 0
        sumando = 1 if cantidad_de_nodos_par else 2
        min = index + sumando * factor
        max = min +2
        subset_de_nodos = nodos_actuales[min:max]
        result = nodo_a_comprobar in subset_de_nodos
        ##print(min, max, subset_de_nodos, sumando, cantidad_de_nodos_par)

        return result

    def pasa_por(self, nodos):
        nodos_actuales = []
        for nodo in self.records:
            nodos_actuales.append(nodo.start_node_str)
            nodos_actuales.append(nodo.end_node_str)
        cantidad_de_nodos_par = not bool(len(nodos) % 2)
        for index, nodo in enumerate(nodos):
            if not self.valida_que_nodo_sigue_en_ruta(index, nodos_actuales, nodo, cantidad_de_nodos_par):
                return False
        ## Esto es para el último salto que no está incluido dentro del loop
        return self.valida_que_nodo_sigue_en_ruta(index, nodos_actuales, nodo, cantidad_de_nodos_par)

    def asegurar_orden_cronologico(self):
        for i in range(len(self.records) - 1):
            if self.records[i+1].start_time < self.records[i].start_time:
                return False
        return True

def esta_ya_en_la_lista(lista, nodo):
    def compara(registro):
        une_estos_satelites = [registro.start_node_str, registro.end_node_str]
        if registro.start_time == nodo.start_time and registro.stop_time and nodo.start_node_str in une_estos_satelites and nodo.end_node_str in une_estos_satelites:
            return True
        return False
    filtrado = list(filter(compara, lista))
    return bool(filtrado)


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
