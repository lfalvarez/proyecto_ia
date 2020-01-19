Proyecto de IA
---
Si uno ejecuta:

```
time python linea_base.py 
```


te muestra algo así
```
el itinerario es así:  ['SCL', 'S1', 'CAL']
De un total de 542 he encontrado 542 rutas_que_funcionan
La ruta que demora menos es:
377 S1 SCL
378 S1 CAL
y se demora 0:17:51.566000

real    0m0.300s
user    0m0.275s
sys     0m0.021s

```

Puedes modificar la cantidad de nodos que te gustaría que visite en el archivo linea_base.py

```time python linea_base.py
el itinerario es así:  ['SCL', 'S1', 'S2', 'CAL']
De un total de 25656 he encontrado 25656 rutas_que_funcionan
La ruta que demora menos es:
126 S1 SCL
129 S2 S1
137 S2 CAL
y se demora 1:52:17.680000

real    0m41.138s
user    0m39.478s
sys     0m1.621s
```

Con dos saltos demora 0.3sec y con 3 se demora 41 segundos. Con 4 saltos se queda pegado todo.