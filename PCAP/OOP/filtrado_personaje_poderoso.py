import random

nombres = ["Arthas", "Merlin", "Legolas", "Diana", "Gimli", "Morgana", "Thalion", "Ezio"]
clases = ["Guerrero", "Mago", "Arquero"]

personajes = [{"nombre": random.choice(nombres),
               "clase": random.choice(clases),
               "nivel": random.randint(1, 10)} 
              for _ in range(10)] 

personajes_poderosos = list(filter(lambda p: p["nivel"] > 5, personajes))

for personaje in personajes_poderosos:
    print(personaje)