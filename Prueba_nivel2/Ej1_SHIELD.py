class ArboldecisionSuperheroe:
    def __init__(self):
        self.arbol = [
            ["¿Es una misión intergaláctica en equipo?", "Khan", "¿Es una misión de destrucción?", "Hulk", "¿Es una misión de defensa o recuperación?", "Capitán América", "¿Es una misión de recuperación donde sea necesario no ser detectado?", "Ant-Man", "¿Es una misión donde se requiera infiltrarse con personas del lugar?", "The Winter Soldier", "¿Es una misión que requiera planificación y manejo de tecnología avanzada?", "Iron Man", "¿Es la próxima acción para tomar y moverse rápidamente de un lugar a otro?", "Nick Fury", "Thor"]
        ]

    def asignar_superheroe(self, mission):
        current_node = 0
        while True:
            valor_nodo = self.arbol[0][current_node]
            if valor_nodo == "Khan":
                return valor_nodo
            if valor_nodo == "Hulk":
                return valor_nodo
            if valor_nodo == "Capitán América":
                return valor_nodo
            if valor_nodo == "Ant-Man":
                return valor_nodo
            if valor_nodo == "The Winter Soldier":
                return valor_nodo
            if valor_nodo == "Iron Man":
                return valor_nodo
            if valor_nodo == "Nick Fury":
                return valor_nodo
            if valor_nodo == "Thor":
                return valor_nodo
            if valor_nodo == "¿Es una misión intergaláctica en equipo?":
                if mission.es_intergalactica_equipo_mision():
                    current_node = 1
                else:
                    current_node = 2
            elif valor_nodo == "¿Es una misión de destrucción?":
                if mission.es_destruccion_mision():
                    current_node = 3
                else:
                    current_node = 4
            elif valor_nodo == "¿Es una misión de defensa o recuperación?":
                if mission.es_defensa_o_recuperacion_mision():
                    current_node = 5
                else:
                    current_node = 6
            elif valor_nodo == "¿Es una misión de recuperación donde sea necesario no ser detectado?":
                if mission.es_robo_recuperacion_mision():
                    current_node = 7
                else:
                    current_node = 8
            elif valor_nodo == "¿Es una misión donde se requiera infiltrarse con personas del lugar?":
                if mission.es_infirtrar_mision():
                    current_node = 9
                else:
                    current_node = 10
            elif valor_nodo == "¿Es una misión que requiera planificación y manejo de tecnología avanzada?":
                if mission.es_tecnologia_avanzada_mision():
                    current_node = 11
                else:
                    current_node = 12
            elif valor_nodo == "¿Es la próxima acción para tomar y moverse rápidamente de un lugar a otro?":
                if mission.is_proxima_accion_moverse_rapido_mision():
                    current_node = 13
                else:
                    current_node = 14
            

class Mision:
    def __init__(self, detalles):
        self.detalles = detalles

    def es_intergalactica_equipo_mision(self):
        return self.detalles.get('tipo') == 'intergalactica' and self.detalles.get('equipo')

    def es_destruccion_mision(self):
        return self.detalles.get('tipo') == 'destruccion'

    def es_defensa_o_recuperacion_mision(self):
        return self.detalles.get('tipo') in ['defensa', 'recuperacion']

    def es_robo_recuperacion_mision(self):
        return self.detalles.get('tipo') == 'recuperacion' and self.detalles.get('robo')

    def es_infirtrar_mision(self):
        return self.detalles.get('tipo') == 'infiltrar'

    def es_tecnologia_avanzada_mision(self):
        return self.detalles.get('tipo') == 'tecnologia_avanzada'

    def is_proxima_accion_moverse_rapido_mision(self):
        return self.detalles.get('tipo') == 'proxima_accion_movimiento_rapido'

if __name__ == "__main__":
    # Asignar un superhéroe a una misión
    arbol = ArboldecisionSuperheroe()
    mision = Mision({'tipo': 'intergalactica', 'equipo': True})
    superheroe = arbol.asignar_superheroe(mision)
    print(f"El superhéroe asignado a esta misión es {superheroe}.")