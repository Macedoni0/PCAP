import random

nombres = ["Arthas", "Merlin", "Legolas", "Diana", "Gimli", "Morgana", "Thalion", "Ezio"]
clases = ["Guerrero", "Mago", "Arquero"]

personajes = [{"nombre": random.choice(nombres),
               "clase": random.choice(clases),
               "nivel": random.randint(1, 10),
               "ataque": random.randint(30, 100)} 
              for _ in range(10)] 

personajes_poderosos = list(filter(lambda p: p["nivel"] > 5, personajes))

personajes_con_ataque_mejorado = list(map(lambda p: {**p, "ataque": p["ataque"] * 1.2 if p["ataque"] > 50 else p["ataque"]}, personajes))

for personaje in personajes_con_ataque_mejorado:
    print(personaje)