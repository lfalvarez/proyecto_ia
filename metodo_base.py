from base import ManagerDeRutas, Ruta
manager = ManagerDeRutas()
manager.leer_registros()
from itertools import combinations


RUTA_ESPERADA = ['SCL', 'S1', 'SCL']

todos_los_links = manager.records

def link_contiene_nodo(link, nodo, links_ya_usados):
    return link.start_node_str == nodo or link.end_node_str == nodo and link.access_id not in links_ya_usados

def obtener_primer_registro_que_tenga_nodo(links_ya_usados, nodo):
    return next((link for link in todos_los_links if link_contiene_nodo(link, nodo, links_ya_usados)), None)

def fuerza_bruta(ruta_objetivo):
    todas_las_rutas = []
    todos_los_ids = list(range(len(todos_los_links)))
    combinaciones = combinations(todos_los_ids, len(ruta_objetivo)) ## Todas las permutaciones posibles
    for combinacion in combinaciones:
        combinacion = list(combinacion)
        r = manager.obtenerRuta(combinacion)
        todas_las_rutas.append(r)
    rutas_que_funcionan = []
    for ruta in todas_las_rutas:
        if(ruta.pasa_por(ruta_objetivo)):
            rutas_que_funcionan.append(ruta)
    print(rutas_que_funcionan[0].records)


ruta_optima = fuerza_bruta(RUTA_ESPERADA)
##print(len(todos_los_links))