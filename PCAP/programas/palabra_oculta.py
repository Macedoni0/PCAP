palabra = input("Introduce palabra a buscar: ").upper()
grupo = input("Introduce grupo de caracteres: ").upper()

contiene = True
inicio=0

for c in palabra:
    pos= grupo.find(c,inicio)
    if pos < 0:
        contiene = False
        break
    inicio = pos + 1
  
    
if contiene:
    print("La palabra está en la cadena")
else:
    print("La palabra no está en la cadena")
        

    


