'''
La función filter() comprueba que los elementos de una serie (ej. una lista) cumplen una condición, 
y devuelve un iterador compuesto por tales elementos.
'''

lista_numerica = [17, -24, 7, 40, -23, 51, 70, 82, -96, 102]

# A partir de la lista de números, crea un filtro que seleccione los números pares, 
# y muestra el resultado en pantalla. 

numero_par = list(filter(lambda x: x % 2 == 0, lista_numerica))

# A partir de la lista de números, crea un filtro que seleccione los números pares > 0, 
# y muestra el resultado en pantalla. 

numero_par_pos = list(filter(lambda x: x % 2 == 0 and x > 0, lista_numerica))

print(numero_par)     # Salida esperada: [-24, 40, 70, 82, -96, 102]
print(numero_par_pos) # Salida esperada: [40, 70, 82, 102]

print("Alvaro Avila Martinez")
