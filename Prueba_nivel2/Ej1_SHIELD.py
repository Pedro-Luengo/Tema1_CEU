class SuperheroDecisionTree:
    def __init__(self):
        self.tree = [
            ["¿Es una misión intergaláctica en equipo?", "Khan", "¿Es una misión de destrucción?", "Hulk", "¿Es una misión de defensa o recuperación?", "Capitán América", "¿Es una misión de recuperación donde sea necesario no ser detectado?", "Ant-Man", "¿Es una misión donde se requiera infiltrarse con personas del lugar?", "The Winter Soldier", "¿Es una misión que requiera planificación y manejo de tecnología avanzada?", "Iron Man", "¿Es la próxima acción para tomar y moverse rápidamente de un lugar a otro?", "Nick Fury", "Thor"]
        ]

    def assign_superhero(self, mission):
        current_node = 0
        while True:
            node_value = self.tree[0][current_node]
            if node_value == "Khan":
                return node_value
            if node_value == "Hulk":
                return node_value
            if node_value == "Capitán América":
                return node_value
            if node_value == "Ant-Man":
                return node_value
            if node_value == "The Winter Soldier":
                return node_value
            if node_value == "Iron Man":
                return node_value
            if node_value == "Nick Fury":
                return node_value
            if node_value == "Thor":
                return node_value
            if node_value == "¿Es una misión intergaláctica en equipo?":
                if mission.is_intergalactic_team_mission():
                    current_node = 1
                else:
                    current_node = 2
            elif node_value == "¿Es una misión de destrucción?":
                if mission.is_destruction_mission():
                    current_node = 3
                else:
                    current_node = 4
            elif node_value == "¿Es una misión de defensa o recuperación?":
                if mission.is_defense_or_recovery_mission():
                    current_node = 5
                else:
                    current_node = 6
            elif node_value == "¿Es una misión de recuperación donde sea necesario no ser detectado?":
                if mission.is_stealth_recovery_mission():
                    current_node = 7
                else:
                    current_node = 8
            elif node_value == "¿Es una misión donde se requiera infiltrarse con personas del lugar?":
                if mission.is_infiltrate_mission():
                    current_node = 9
                else:
                    current_node = 10
            elif node_value == "¿Es una misión que requiera planificación y manejo de tecnología avanzada?":
                if mission.is_advanced_tech_mission():
                    current_node = 11
                else:
                    current_node = 12
            elif node_value == "¿Es la próxima acción para tomar y moverse rápidamente de un lugar a otro?":
                if mission.is_next_action_move_quickly_mission():
                    current_node = 13
                else:
                    current_node = 14
            

class Mission:
    def __init__(self, details):
        self.details = details

    def is_intergalactic_team_mission(self):
        return self.details.get('type') == 'intergalactic' and self.details.get('team')

    def is_destruction_mission(self):
        return self.details.get('type') == 'destruction'

    def is_defense_or_recovery_mission(self):
        return self.details.get('type') in ['defense', 'recovery']

    def is_stealth_recovery_mission(self):
        return self.details.get('type') == 'recovery' and self.details.get('stealth')

    def is_infiltrate_mission(self):
        return self.details.get('type') == 'infiltrate'

    def is_advanced_tech_mission(self):
        return self.details.get('type') == 'advanced_tech'

    def is_next_action_move_quickly_mission(self):
        return self.details.get('type') == 'next_action_move_quickly'

if __name__ == "__main__":
    # Asignar un superhéroe a una misión
    tree = SuperheroDecisionTree()
    mission = Mission({'type': 'recovery', 'team': True})
    superhero = tree.assign_superhero(mission)
    print(f"El superhéroe asignado a esta misión es {superhero}.")