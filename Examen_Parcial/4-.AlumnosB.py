class alumno:
    #Usamos el constructor para asignarle nombre y nota al alumno
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        #Cuando se cree el alumno se muestra esta confirmación
        print(f"El alumno {self.nombre} se ha inscrito con exito. ")

    #Metodo especial para que muestre la imformacion de un alumno
    def __str__(self):
        return f"Nombre: {self.nombre}\t  Nota: {self.nota}"

    #Metodo que te dice si has aprobado en funcion de la calificacion del alumno
    def calificacion(self):
        if self.nota >= 5 and self.nota<= 10:
            print(f"El alumno {self.nombre} ha aprobado la asignatura. ")
        elif self.nota <5 and self.nota >=0:
            print(f"El alumno {self.nombre} ha suspendido la asignatura. ")
        else:
            print(f"El alumno {self.nombre} no ha obtenido una calificación válida.")

#Creamos los alumnos      
Dario = alumno("Dario", 5)
Javi = alumno("Javier", 7)
Mareque = alumno("Mareque", 4)
#Mostramos la informacion de cada alumno
print(Mareque)
print(Javi)
print(Dario)