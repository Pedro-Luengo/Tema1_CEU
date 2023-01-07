class Request:
    def __init__(self, khan, universe, description):
        self.khan = khan
        self.universe = universe
        self.description = description

class KhanDecisionQueue:
    def __init__(self):
        self.high_priority_queue = []
        self.medium_priority_queue = []
        self.low_priority_queue = []
        self.queue = [[] for _ in range(3)]
        self.bitacora = []

    def add_to_bitacora(self):
        added = False
        while not added:
            if len(self.high_priority_queue) > 0:
                self.bitacora.append(f"Nombre de Khan: {self.high_priority_queue[0].khan}. Universo: {self.high_priority_queue[0].universe}. Descripción: {self.high_priority_queue[0].description}")
                added = True
            elif len(self.medium_priority_queue) > 0:
                self.bitacora.append(f"Nombre de Khan: {self.medium_priority_queue[0].khan}. Universo: {self.medium_priority_queue[0].universe}. Descripción: {self.medium_priority_queue[0].description}")
                added = True
            elif len(self.low_priority_queue) > 0:
                self.bitacora.append(f"Nombre de Khan: {self.low_priority_queue[0].khan}. Universo: {self.low_priority_queue[0].universe}. Descripción: {self.low_priority_queue[0].description}")
                added = True

    def __iter__(self):
        return self

    def __next__(self):
        request = self.dequeue()
        if request is not None:
            return request
        raise StopIteration

    def add_request_to_queue(self, request):
        self.queue.append(request)
    
    def enqueue(self, request):
        if request.khan == "Gran Conquistador" or request.universe == "616" or "El que permanece" in request.description:
            self.queue[0].append(f"El Khan es: {request.khan}. El universo es: {request.universe}. La descripción es: {request.description}.")
        elif request.khan == "Khan que todo lo sabe" or "Carnicero de Dioses" in request.description or request.universe == "838":
            self.queue[1].append(f"El Khan es: {request.khan}. El universo es: {request.universe}. La descripción es: {request.description}.")
        else:
            self.queue[2].append(f"El Khan es: {request.khan}. El universo es: {request.universe}. La descripción es: {request.description}.")
        
        

    def dequeue(self):
        for i, requests in enumerate(self.queue):
            if requests:
                return self.queue[i].pop(0)
        return None

    def review_log(self):
        return self.bitacora

def print_request(request):
    print(f"Nombre de Khan: {request.khan}")
    print(f"Universo: {request.universe}")
    print(f"Descripción: {request.description}")

if __name__ == "__main__":

    queue = KhanDecisionQueue()

    queue.high_priority_queue.append(Request("Gran Conquistador", "616", "El que permanece"))
    queue.medium_priority_queue.append(Request("Khan que todo lo sabe", "838", "Carnicero de Dioses"))
    queue.low_priority_queue.append(Request("Khan de otro universo", "123", "Otro pedido"))

    for i in queue.high_priority_queue + queue.medium_priority_queue + queue.low_priority_queue:
        queue.enqueue(i)
    
    for request in queue.high_priority_queue or queue.medium_priority_queue or queue.low_priority_queue:
        queue.add_to_bitacora()
    print(queue.queue)
    print(queue.bitacora)