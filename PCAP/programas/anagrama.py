while True:
    text1 = input("Introduce la 1º palabra: ").upper()
    if not text1.isalpha():
        print(f"Error, la palabra '{text1}' debe ser alfabética.")
        break
    text2 = input("Introduce la 2º palabra: ").upper()
    if not text2.isalpha():
        print(f"Error, la palabra '{text2}' debe ser alfabética.")
        break

    if sorted(text1) == sorted(text2):
        print("Las palabras" + " "+ text1 +" "+ "y" +" "+ text2 +" "+ "son anagramas")
        break
    else:
        print("Las palabras" +" "+text1+" "+"y"+" " +text2+" "+ "no son anagramas")
        break


