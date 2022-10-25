class producto:

    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

    def __str__(self):
        return "{}\t{}\t{}\t {}".format(self.codigo, self.nombre, self.precio, self.tipo)

    def añadir(self):
        self.añadido = True
        if self.añadido == True:
            print(f"El producto: {self.nombre} se ha añadido con exito. ")
        else:
            print(f"El producto: {self.nombre} no se ha añadido con exito. ")    

Producto_1 = producto(codigo="#994889", nombre="Tablet", precio="200€", tipo="Electronica")
print(Producto_1)
print(Producto_1.nombre)
print(type(Producto_1))
producto.añadir(Producto_1)
print(Producto_1.añadido)