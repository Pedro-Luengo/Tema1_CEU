from datetime import datetime
from time import sleep

def reloj():
    # Obtenemos la hora actual
    hora_actual = datetime.now()
    # Obtenemos las horas, minutos y segundos
    horas = hora_actual.hour
    minutos = hora_actual.minute
    segundos = hora_actual.second
    # Mostramos la hora actual en el formato HH:MM:SS
    print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

# Ejecutamos la función en un bucle infinito
while True:
    # Mostramos la hora actual
    reloj()
    # Esperamos un segundo
    sleep(1)