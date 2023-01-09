from typing import List

class Request:
    def __init__(self, name: str, universe: str, description: str):
        self.name = name
        self.universe = universe
        self.description = description
        self.priority = self.set_priority()
    
    def set_priority(self) -> int:
        if self.name == "Gran Conquistador" or self.universe == "616" or "El que permanece" in self.description:
            return 3
        elif self.name == "Khan que todo lo sabe" or "Carnicero de Dioses" in self.description or self.universe == "838":
            return 2
        else:
            return 1

class QueueManager:
    def __init__(self):
        self.queue = []
        self.log = []
    
    def add_request(self, request: Request):
        self.queue.append(request)
    
    def process_next_request(self):
        request = self.queue.pop(0)
        if request.priority == 3:
            self.log.append(request)
        else:
            # process request
            pass

def run_queue_manager(queue_manager: QueueManager):
    while queue_manager.queue:
        queue_manager.process_next_request()

# Ejemplo de uso
queue_manager = QueueManager()
queue_manager.add_request(Request("Gran Conquistador", "616", "Necesito ayuda para vencer a El que permanece"))
queue_manager.add_request(Request("Khan que todo lo sabe", "838", "Tengo un problema con el Carnicero de Dioses"))
queue_manager.add_request(Request("Khan X", "999", "Necesito sugerencias para conquistar mi universo"))
run_queue_manager(queue_manager)

# Ver bitácora de pedidos de mayor prioridad
for request in queue_manager.log:
    print(f"Solicitante: {request.name}")
    print(f"Multiverso: {request.universe}")
    print(f"Descripción: {request.description}")