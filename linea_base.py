from base import ManagerDeRutas, Ruta
manager = ManagerDeRutas()
manager.leer_registros()
from itertools import combinations


RUTA_ESPERADA = ['SCL', 'S1', 'S2','CAL']

todos_los_links = manager.records

def genera_filters(index, nodos_que_deberia_unir):
    def prueba(ruta):
        link = ruta.records[index]
        nodos_que_une = [link.start_node_str, link.end_node_str]
        if nodos_que_deberia_unir[0] not in nodos_que_une:
            return False
        if nodos_que_deberia_unir[1] not in nodos_que_une:
            return False
        return True
    return prueba

def obtener_rutas_correctas(combinaciones, ruta_objetivo, todas_las_rutas):
    for combinacion in combinaciones:
        combinacion = list(combinacion)
        r = manager.obtenerRuta(combinacion)
        todas_las_rutas.append(r)
    for i in range(len(ruta_objetivo) - 1):
        nodos_que_deberia_unir = [ruta_objetivo[i], ruta_objetivo[i + 1]]
        filtro = genera_filters(i, nodos_que_deberia_unir)
        todas_las_rutas = list(filter(filtro, todas_las_rutas))
    rutas_que_funcionan = []
    for ruta in todas_las_rutas:
        if ruta.asegurar_orden_cronologico():
            rutas_que_funcionan.append(ruta)
    return rutas_que_funcionan, todas_las_rutas

def fuerza_bruta(ruta_objetivo):
    todas_las_rutas = []
    todos_los_ids = list(range(len(todos_los_links)))
    combinaciones = combinations(todos_los_ids, len(ruta_objetivo) - 1) ## Todas las permutaciones posibles
    rutas_que_funcionan, todas_las_rutas = obtener_rutas_correctas(combinaciones, ruta_objetivo, todas_las_rutas)
    print('el itinerario es así: ', ruta_objetivo)
    print('De un total de {total} he encontrado {numero} rutas_que_funcionan'.format(numero=len(rutas_que_funcionan), total=len(todas_las_rutas)))
    rutas_que_funcionan[0].pasa_por(ruta_objetivo)
    ruta_que_demora_menos = rutas_que_funcionan[0]
    for ruta in rutas_que_funcionan:
        if ruta.se_demora() < ruta_que_demora_menos.se_demora():
            ruta_que_demora_menos = ruta
    print('La ruta que demora menos es:')
    for link in ruta_que_demora_menos.records:
        print(link.access_id, link.start_node_str, link.end_node_str)
    print('y se demora {tiempo}'.format(tiempo=ruta_que_demora_menos.se_demora()))
    return ruta_que_demora_menos



ruta_optima = fuerza_bruta(RUTA_ESPERADA)
##print(len(todos_los_links))