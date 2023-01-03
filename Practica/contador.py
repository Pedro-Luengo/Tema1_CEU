import sys

##Creamos la función para leer el fichero
def leer_fichero():
    # Abrimos el fichero en modo lectura
    try:
        with open("contador.txt", "r") as f:
            # Leemos el contenido del fichero
            contenido = f.read()
            # Si el fichero está vacío o no existe, retornamos 0
            if not contenido:
                return 0
            # Si el fichero no está vacío, retornamos el valor del contador como número
            return int(contenido)
    except:
        print("Error: Fichero corrupto.")
        sys.exit(1)

##Creamos la función para escribir el fichero
def escribir_fichero(valor):
    # Abrimos el fichero en modo escritura
    try:
        with open("contador.txt", "w") as f:
            # Escribimos el valor del contador en el fichero
            f.write(str(valor))
    except:
        print("Error: Fichero corrupto.")
        sys.exit(1)

    ##Comprobamos si se ha pasado algún argumento
    if len(sys.argv) > 1:
    # Si se ha pasado el argumento inc, incrementamos el contador
        if sys.argv[1] == "inc":
            # Leemos el valor actual del contador
            contador = leer_fichero()
            # Incrementamos el contador en uno
            contador += 1
    else:
        # Si no se ha pasado ningún argumento o se ha pasado un argumento que no es ni inc ni dec
        # Leemos el valor actual del contador
        contador = leer_fichero()
        # Mostramos el valor del contador por pantalla
        print(contador)


