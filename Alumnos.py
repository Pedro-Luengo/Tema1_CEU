class alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno se ha inscrito con exito. ")

    def __str__(self):
        return f"{self.nombre} \t {self.nota}"

    def calificacion(self):
        if self.nota >= 5 and self.nota<= 10:
            print("El alumno ha aprobado la asignatura. ")
        elif self.nota <5 and self.nota >=0:
            print("El alumno ha suspendido la asignatura. ")
        else:
            print("El alumno no ha obtenido una calificación válida.")
    
Dario = alumno("Dario", 5)
Javi = alumno("Javier", 7)
Mareque = alumno("Mareque", 4)
print(Mareque)
alumno.calificacion(Mareque)