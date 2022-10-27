## Ejercicio 4
'''
Durante la planificación de un proyecto se han acordado una lista de tareas.
Para cada una de estas tareas se ha asignado un orden de prioridad 
(cuanto menor es el número de orden, más prioridad).

¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas
pero sin los números de orden?

Sugerencia

Para ordenar automáticamente una lista es posible utilizar el método .sort(), 
deberias probarlo.
'''
import operator
def ordenar():

    cola = (
            {'tarea': 'comprar', 'prioridad': 1},
            {'tarea': 'comer', 'prioridad': 4 },
            {'tarea': 'poner la mesa', 'prioridad': 3 },
            {'tarea': 'cocinar', 'prioridad': 2 }
            )
    orden = []
    tareas = []
    for i in range(len(cola)):
        orden.append(cola[i]['prioridad'])
    orden = sorted(orden)
    for i in (range(len(orden)+1)):
        for n in (range(len(cola))):
            if i == cola[n]['prioridad']:
                tareas.append(cola[n]['tarea'])
    print(tareas)
ordenar()