fecha = ''

while True:
    fecha = input("Ingrese la fecha de nacimiento AAAAMMDD: ")
    if fecha.isnumeric() and len(fecha) == 8:
        break
    print("Debes introducir una fecha en formato AAAAMMDD (8 dígitos).")

digito = 0
suma = 0

for c in fecha:
    suma += int(c)

if suma >= 10:
    for c in str(suma):
        digito += int(c)
else:
    digito = suma

print("La suma de todos los dígitos de la fecha es: " + str(digito))
