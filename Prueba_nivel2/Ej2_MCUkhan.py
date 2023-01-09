class Request:
    def __init__(self, khan, universo, descripcion):
        self.khan = khan
        self.universo = universo
        self.descripcion = descripcion

class KhanDecisionCola:
    def __init__(self):
        self.alta_prioridad_cola = []
        self.media_prioridad_cola = []
        self.baja_prioridad_cola = []
        self.cola = [[] for _ in range(3)]
        self.bitacora = []

    def add_to_bitacora(self):
        added = False
        while not added:
            if len(self.alta_prioridad_cola) > 0:
                self.bitacora.append(f"Nombre de Khan: {self.alta_prioridad_cola[0].khan}. Universo: {self.alta_prioridad_cola[0].universo}. Descripción: {self.alta_prioridad_cola[0].descripcion}")
                added = True
            elif len(self.media_prioridad_cola) > 0:
                self.bitacora.append(f"Nombre de Khan: {self.media_prioridad_cola[0].khan}. Universo: {self.media_prioridad_cola[0].universo}. Descripción: {self.media_prioridad_cola[0].descripcion}")
                added = True
            elif len(self.baja_prioridad_cola) > 0:
                self.bitacora.append(f"Nombre de Khan: {self.baja_prioridad_cola[0].khan}. Universo: {self.baja_prioridad_cola[0].universe}. Descripción: {self.baja_prioridad_cola[0].descripcion}")
                added = True

    def __iter__(self):
        return self

    def __next__(self):
        request = self.decolar()
        if request is not None:
            return request
        raise StopIteration

    def add_request_to_queue(self, request):
        self.cola.append(request)
    
    def encolar(self, request):
        if request.khan == "Gran Conquistador" or request.universo == "616" or "El que permanece" in request.descripcion:
            self.cola[0].append(f"El Khan es: {request.khan}. El universo es: {request.universo}. La descripción es: {request.descripcion}.")
        elif request.khan == "Khan que todo lo sabe" or "Carnicero de Dioses" in request.descripcion or request.universo == "838":
            self.cola[1].append(f"El Khan es: {request.khan}. El universo es: {request.universo}. La descripción es: {request.descripcion}.")
        else:
            self.cola[2].append(f"El Khan es: {request.khan}. El universo es: {request.universo}. La descripción es: {request.descripcion}.")
        
        

    def decolar(self):
        for i, requests in enumerate(self.cola):
            if requests:
                return self.cola[i].pop(0)
        return None

    def review_log(self):
        return self.bitacora

def print_request(request):
    print(f"Nombre de Khan: {request.khan}")
    print(f"Universo: {request.universo}")
    print(f"Descripción: {request.descripcion}")

if __name__ == "__main__":

    cola = KhanDecisionCola()

    cola.alta_prioridad_cola.append(Request("Gran Conquistador", "616", "El que permanece"))
    cola.media_prioridad_cola.append(Request("Khan que todo lo sabe", "838", "Carnicero de Dioses"))
    cola.baja_prioridad_cola.append(Request("Khan de otro universo", "123", "Otro pedido"))

    for i in cola.alta_prioridad_cola + cola.media_prioridad_cola + cola.baja_prioridad_cola:
        cola.encolar(i)
    
    for request in cola.alta_prioridad_cola or cola.media_prioridad_cola or cola.baja_prioridad_cola:
        cola.add_to_bitacora()
    print(cola.cola)
    print(cola.bitacora)