#cifrado cesar
text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha():      #Si no es una cifra, pasa
        continue
    char = char.upper()         #m --> M
    code = ord(char) + 1        #punto de código siguiente    
    if code > ord('Z'):         #Si rebasa el alfabeto...
        code = ord('A')         #... empieza otra vez.
    cipher += chr(code)

print(cipher)
    
