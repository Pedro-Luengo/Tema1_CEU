class alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print(f"El alumno {self.nombre} se ha inscrito con exito. ")

    def __str__(self):
        return f"{self.nombre}  {self.nota}"

    def calificacion(self):
        if self.nota >= 5 and self.nota<= 10:
            print(f"El alumno {self.nombre} ha aprobado la asignatura. ")
        elif self.nota <5 and self.nota >=0:
            print(f"El alumno {self.nombre} ha suspendido la asignatura. ")
        else:
            print(f"El alumno {self.nombre} no ha obtenido una calificación válida.")
    
Dario = alumno("Dario", 5)
Javi = alumno("Javier", 7)
Mareque = alumno("Mareque", 4)
print(Mareque)
alumno.calificacion(Mareque)
alumno.calificacion(Javi)
Javi.nota = 7
alumno.calificacion(Javi)