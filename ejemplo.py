from base import ManagerDeRutas

manager = ManagerDeRutas()
manager.leer_registros()
ruta = manager.obtenerRuta([192, 196, 198])
print('los registros son:')
for registro in ruta.records:
    print('el registro es el', registro)
print('esos eran.')

print('La ruta se demora: ', ruta.se_demora())
print('Pasa la ruta por S1, CAL, S1????? ', ruta.pasa_por(['S1', 'CAL', 'S2']))

'''
los registros son:
el registro es el 192, S1, 1, SCL, 3, 2019-06-20 22:52:23.795000, 2019-06-20 23:03:48.437000
el registro es el 196, S2, 2, S1, 1, 2019-06-20 23:06:54.403000, 2019-06-20 23:18:40.673000
el registro es el 198, S1, 1, S2, 2, 2019-06-20 23:54:17.133000, 2019-06-21 00:06:03.527000
esos eran.
La ruta se demora:  1:01:53.338000
Pasa la ruta por S1, CAL, S1?????  False

'''