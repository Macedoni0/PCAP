import random

nombres = ["Arthas", "Merlin", "Legolas", "Diana", "Gimli", "Morgana", "Thalion", "Ezio"]
clases = ["Guerrero", "Mago", "Arquero"]

personajes = [{"nombre": random.choice(nombres),
               "clase": random.choice(clases),
               "nivel": random.randint(1, 10)} 
              for _ in range(5)]

test = personajes
for personaje in test:
    print(personaje)
