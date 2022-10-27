class producto:

    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

    def __str__(self):
        return "{} \t {} \t {} \t {}".format(self.codigo, self.nombre, self.precio, self.tipo)

    def añadir(self):
        self.añadido = True
        if self.añadido == True:
            print(f"El producto: {self.nombre} se ha añadido con exito. ")
        else:
            print(f"El producto: {self.nombre} no se ha añadido con exito. ")    

Producto_1 = producto(codigo="#974529", nombre="movil", precio="1200€", tipo="Electronica")
Producto_2 = producto(codigo="#874932", nombre="sudadera", precio="80€", tipo="Ropa")
Producto_3 = producto(codigo="#874933", nombre="pantalon", precio="110€", tipo="Ropa")
print(Producto_1)
print(Producto_1.nombre)
Producto_1.nombre = "samsung"
print(Producto_1.nombre)
print(type(Producto_1))
producto.añadir(Producto_2)
print(Producto_2.añadido)
