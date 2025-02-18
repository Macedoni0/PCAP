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

def generador_loteria():
    numeros = random.sample(range(1, 50), 6) 
    for numero in numeros:
        yield numero

for personaje in personajes_con_ataque_mejorado:
    print(personaje)

generador = generador_loteria()
numeros_loteria = [num for num in generador]
print("Números de lotería generados:", numeros_loteria)

def contador_puntuaciones():
    puntuacion = 0
    def incrementar():
        nonlocal puntuacion
        puntuacion += 1
        return puntuacion
    return incrementar

contador = contador_puntuaciones()

print("Puntuación actual:", contador())
print("Puntuación actual:", contador())
print("Puntuación actual:", contador())
