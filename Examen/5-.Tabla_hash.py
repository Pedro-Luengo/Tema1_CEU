class hash_tabla():

    #En primer lugar creo un constructor donde se crea la tabla hash de un determinado tamaño: tamaño_tab 
    def __init__(self, tamaño_tabla):
        self.tamaño_tabla = tamaño_tabla
        self.tabla = [None] * tamaño_tabla

    #Creamos un metodo que nos permitira imprimir esa tabla
    def imprime_tabla(self):
        for i in range (len(self.tabla)):
            print ("{}: {}".format(i, self.tabla[i]))

    #Ahora calculamos la funcion hash de una cadena. Para ello asigno un valor de la tabla a cada caracter.
    #viendo la funcion bernstein, usamos el numero magico(33)
    def funcion_hash(self, caracter):
        return ord(caracter) * 33 % self.tamaño_tabla
    
    #Método para ingresar elementos
    def Insertar_elementos(self, valor):
        #Calcula la posicion de la tabla
        hash = self.funcion_hash(valor)
        #Si esta vacía lo añade.
        if self.tabla[hash] is None:
            self.tabla[hash] = valor

    #Calcula el código hash de cada elemento de la cadena y le sumo 33 para convertirlo a caracteres imprimibles.
    def encriptar(self, cadena):
        resultado = ""
        for i in cadena:
            self.Insertar_elementos(i)
            resultado = resultado + chr(self.funcion_hash(i)+33)
        return resultado

    #A partir de una cadena hasheada te devuelve la cadena original
    def des_encriptar(self, cadena):
        resultado = ""
        for i in cadena:
            resultado = resultado +str(self.tabla[ord(i)-33])
        return resultado

alfabeto = [chr(i) for i in range(32, 125)]
#Lo primero es crear la tabla hash del tamaño de la longitud del alfabeto
A = hash_tabla(len(alfabeto))
#Para comprobar si la tabal hash se creo correctamente probamos a insertar un valor y a imprimir la tabla:
#A.Insertar_elementos("A")
#A.imprime_tabla()

#Solucion ejercicio:
#Pedimos la cadena que queremos encriptar
cadena = input("Introduce una cadena: ")
print(f"Cadena sin encriptar: {cadena}")
#Encriptamos la cadena y la mostramos:
cadena_encriptada = A.encriptar(cadena)
print(f"Cadena encriptada: {cadena_encriptada}")
#Desencriptamos y mostramos la cadena normal:
cadena_desencriptada = A.des_encriptar(cadena_encriptada)
print(f"Cadena desencriptada: {cadena_desencriptada}")

    
