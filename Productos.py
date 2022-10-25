class producto:
    def _init_(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

    def _str_(self):
        return "{} {} {} {}".format(self.codigo, self.nombre, self.precio, self.tipo)

    def añadir(self):
        self.añadido = True
        if self.añadido == True:
            print(f"El producto: {self.nombre} se ha añadido con exito. ")
        else:
            print(f"El producto: {self.nombre} no se ha añadido con exito. ")    

        Producto_1 = producto("#994889", "Tablet", "200€", "Electronica")
        print(Producto_1.nombre)
        print(type(Producto_1))
        producto.añadir(Producto_1)
        print(Producto_1.añadido)