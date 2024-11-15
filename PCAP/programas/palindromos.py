frase = input("Introduce una frase: ")
frase2 = (frase.lower()).replace(' ','')
if frase2 == frase2[::-1]:
    print("la frase es un palindromo")
else:
    print("la frase no es un palindromo")

print(frase2)
