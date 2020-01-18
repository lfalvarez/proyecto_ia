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