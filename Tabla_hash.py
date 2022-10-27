class hash_tabla():
    #En primer lugar creo un constructor donde se crea la tabla hash de un determinado tamaño: tamaño_tab 
    def _init_(self, tamaño_tab):
        self.tamaño_tab = tamaño_tab
        self.tabla = [None] * tamaño_tab

    def imprime_tabla(self):
        for i in range (len(self.tabla)):
            print ("{}: {}".format(i, self.tabla[i]))

    #Calcula la función hash de una cadena.
    #Asigno un valor de la tabla hash a cada caracter
    #Nos basamos en la función de Bernstein, el número 33 es conocido como el número mágico.
    def funcion_hash(self, caracter):
        return ord(caracter) * 33 % self.tamaño_tab
    
    #Método para ingresar elementos
    #Añade en la posición de la tabla hash corresppondiente el elemento.
    def Insertar_elementos(self, valor):
        #Calcula la posición de la tabla
        hash = self.funcion_hash(valor)
        #Si esta posición esta vacía lo añade.
        if self.tabla[hash] is None:
            self.tabla[hash] = valor

    #Calcula el código hash de cada elemento de la cadena y le sumo 33 para convertirlo a caracteres imprimibles.
    #Devuelve la cadena hasheada
    def encriptar(self, cadena):
        resultado = ""
        for i in cadena:
            self.Insertar_elementos(i)
            resultado = resultado + chr(self.funcion_hash(i)+33)
        return resultado

    #A partir de una cadena hasheada te devuelve la cadena en claro.
    def des_encriptar(self, cadena):
        resultado = ""
        for i in cadena:
            resultado = resultado +str(self.tabla[ord(i)-33])
        return resultado

alfabeto = [chr(i) for i in range(32, 125)]
#Lo primero es crear la tabla hash del tamaño de la longitud del alfabeto
A = hash_tabla(len(alfabeto))
#Inserto un elemento en la tabla hash
A.Insertar_elementos("A")
#Imprime la tabla hash para comprobado que se han insertado bien los elementos
A.imprime_tabla()

#Imprime una palabra encriptada
cadena = input("Introduce una cadena: ")
print(f"Cadena sin encriptar: {cadena}")
cadena_encriptada = A.encriptar(cadena)
print(f"Cadena encriptada: {cadena_encriptada}")
cadena_desencriptada = A.des_encriptar(cadena_encriptada)
print(f"Cadena desencriptada: {cadena_desencriptada}".format(cadena_desencriptada))

    
