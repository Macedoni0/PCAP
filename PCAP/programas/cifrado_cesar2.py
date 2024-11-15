text= input("Ingresa tu mensaje:")

shift = 0
while shift == 0:
    try:
        shift = int(input("Ingresa el valor de cambio de cifrado: "))
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        print("Error: valor de cambio invalido")
        shift = 0

cipher = ''
for char in text:
    code = ord(char) + shift
    if char.isupper():
        first = ord('A')
    else:
        first = ord('a')
    
    code = (code - first) % 26

    cipher += chr(first + code)

print(cipher)
        


