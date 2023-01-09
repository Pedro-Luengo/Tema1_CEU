from typing import List

class Peticion:
    def __init__(self, nombre: str, universo: str, descripcion: str):
        self.nombre = nombre
        self.universo = universo
        self.descripcion = descripcion
        self.prioridad = self.determinar_prioridad()
    
    def determinar_prioridad(self):
        if self.nombre == "Gran Conquistador" or self.universo == "616" or "El que permanece" in self.descripcion:
            return 3
        elif self.nombre == "Khan que todo lo sabe" or "Carnicero de Dioses" in self.descripcion or self.universo == "838":
            return 2
        else:
            return 1

class AdministrarColas:
    def __init__(self):
        self.cola = []
        self.log = []
    
    def añadir_peticion(self, peticion: Peticion):
        self.cola.append(peticion)
    
    def procesar_siguiente_peticion(self):
        # Buscar la siguiente petición de mayor prioridad en la cola
        request = self.cola[0]
        for r in self.cola:
            if r.prioridad > request.prioridad:
                request = r
        # Eliminar la petición de mayor prioridad de la cola
        self.cola.remove(request)
        # Añadir la petición de mayor prioridad al log
        self.log.append(request)
        # Procesar la petición
        pass

def ejecutar_administrador_colas(administrador_colas: AdministrarColas):
    # Procesar y eliminar sólo la primera petición de mayor prioridad de la lista self.cola
    if administrador_colas.cola:
        administrador_colas.procesar_siguiente_peticion()

# Ejemplo de uso
administrar_colas = AdministrarColas()
administrar_colas.añadir_peticion(Peticion("Gran Conquistador", "616", "Necesito ayuda para vencer a El que permanece"))
administrar_colas.añadir_peticion(Peticion("Khan que todo lo sabe", "838", "Tengo un problema con el Carnicero de Dioses"))
administrar_colas.añadir_peticion(Peticion("Khan X", "999", "Necesito sugerencias para conquistar mi universo"))
ejecutar_administrador_colas(administrar_colas)

# Ver bitácora de pedidos de mayor prioridad
for pedido in administrar_colas.log:
    print(f"Solicitante: {pedido.nombre}")
    print(f"Multiverso: {pedido.universo}")
    print(f"Descripción: {pedido.descripcion}")