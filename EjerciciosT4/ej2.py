import random
from queue import PriorityQueue

class Mission:
    def __init__(self, type, planet, general):
        self.type = type
        self.planet = planet
        self.general = general
    
    def is_high_priority(self):
        return self.general in ['Palpatine', 'Darth Vader']
    
    def __lt__(self, other):
        # Comparar las misiones según su prioridad
        return self.is_high_priority() and not other.is_high_priority()
    

class MissionManager:
    def __init__(self):
        self.vehicles = ['AT-AT', 'AT-RT', 'AT-TE', 'AT-DP', 'AT-ST', 'AT-M6', 'AT-MP', 'AT-DT']
        self.queue = PriorityQueue()
    
    def add_mission(self, mission):
        # Añadir la misión a la cola de prioridad
        self.queue.put((mission.is_high_priority(), mission))
    
    def assign_resources(self):
        # Asignar recursos a todas las misiones de la cola
        while not self.queue.empty():
            # Obtener la misión de mayor prioridad
            _, mission = self.queue.get()
            
            if mission.is_high_priority():
                # Asignar recursos manualmente
                print(f'Asignando recursos manualmente a la misión de tipo {mission.type} solicitada por {mission.general}')
            else:
                if mission.type == 'exploración':
                    # Asignar 15 Scout Troopers y 2 speeder bike
                    print(f'Asignando 15 Scout Troopers y 2 speeder bike a la misión de exploración a {mission.planet} solicitada por {mission.general}')
                elif mission.type == 'contención':
                    # Asignar 30 Stormtroopers y tres vehículos aleatorios
                    vehicles = [self.get_random_vehicle() for _ in range(3)]
                    print(f'Asignando 30 Stormtroopers y los vehículos {vehicles} a la misión de contención a {mission.planet} solicitada por {mission.general}')
                elif mission.type == 'ataque':
                    # Asignar 50 Stormtroopers y siete vehículos aleatorios
                    vehicles = [self.get_random_vehicle() for _ in range(7)]
                    print(f'Asignando 50 Stormtroopers y los vehículos {vehicles} a la mision de ataque a {mission.planet} solicitada por {mission.general}')
    
    def get_random_vehicle(self):
        return random.choice(self.vehicles)

# Crear una instancia de MissionManager
manager = MissionManager()

# Crear algunas misiones
mission1 = Mission('exploración', 'Tatooine', 'Leia Organa')
mission2 = Mission('contención', 'Alderaan', 'Mon Mothma')
mission3 = Mission('ataque', 'Coruscant', 'Darth Vader')
mission4 = Mission('exploración', 'Naboo', 'Padmé Amidala')
mission5 = Mission('contención', 'Kamino', 'Palpatine')

# Añadir las misiones a la cola de prioridad del MissionManager
manager.add_mission(mission1)
manager.add_mission(mission2)
manager.add_mission(mission3)
manager.add_mission(mission4)
manager.add_mission(mission5)

# Asignar recursos a las misiones
manager.assign_resources()