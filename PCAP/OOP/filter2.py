'''
Ejemplo simple de uso de filtro (filter).
'''

import random

# Genera una lista de 10 números aleatorios entre -10 y 10
num_aleatorios = [random.randint(-10, 10) for _ in range(10)]

# Crea un filtro que seleccione los números pares positivos
pares_positivos = list(filter(lambda x: x % 2 == 0 and x > 0, num_aleatorios))

print(num_aleatorios) 
print(pares_positivos) 

print("Alvaro Avila Martinez")