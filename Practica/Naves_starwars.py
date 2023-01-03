from operator import itemgetter
naves = [{"nombre": "Halcón Milenario", "largo": 34.75, "tripulacion": 4, "pasajeros": 75},
{"nombre": "Caza TIE", "largo": 9.09, "tripulacion": 1, "pasajeros": 0},
{"nombre": "Crucero Estelar Mon Calamari", "largo": 122, "tripulacion": 20596, "pasajeros": 7500},
{"nombre": "Estrella de la Muerte", "largo": 120000, "tripulacion": 474000, "pasajeros": 100000},
{"nombre": "Nave transporte AT-AT", "largo": 20.5, "tripulacion": 20, "pasajeros": 40},
{"nombre": "Nave transporte AT-ST", "largo": 10.5, "tripulacion": 10, "pasajeros": 20},
{"nombre": "Nave AT-PT", "largo": 6.5, "tripulacion": 3, "pasajeros": 6},
{"nombre": "Nave AT-XT", "largo": 8.5, "tripulacion": 4, "pasajeros": 8},
{"nombre": "Nave transporte AT-DP", "largo": 12.5, "tripulacion": 15, "pasajeros": 30}]


naves_ordenadas = sorted(naves, key=itemgetter('largo'))
print(naves_ordenadas)