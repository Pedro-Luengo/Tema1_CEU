class producto:
    def _init_(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

    def _str_(self):
        return "{} {} {} {}".format(self.codigo, self.nombre, self.precio, self.tipo)
    
        