import random
import string

class PersonajeGacha:
    def __init__(self, nombre, rareza, elemento):
        self.nombre = nombre
        self.rareza = rareza
        self.elemento = elemento
        self.__id_secreto = self.generar_id_secreto()
    
    def __str__(self):
        return f"{self.nombre} ({self.rareza}) - Elemento: {self.elemento}"
    
    def generar_id_secreto(self):
        letras = ''.join(random.choices(string.ascii_uppercase, k=2))
        numeros = ''.join(random.choices(string.digits, k=3))
        return letras + numeros
    
    @staticmethod
    def invocar():
        probabilidades = {
            5: 0.05, 
            4: 0.15,  
            3: 0.80   
        }
        personajes_disponibles = {
            5: ["Diluc", "Jean", "Mona", "Keching", "Qiqi"],
            4: ["Razor", "Sucrose", "Chongyun", "Diona", "Fischl"],
            3: ["Kaeya", "Lisa", "Amber", "Noelle", "Xiangling"]
        }
        
        rareza_elegida = random.choices([5, 4, 3], weights=[probabilidades[5], probabilidades[4], probabilidades[3]])[0]
        nombre = random.choice(personajes_disponibles[rareza_elegida])
        elemento = random.choice(["Pyro", "Hydro", "Electro", "Cryo", "Geo", "Anemo", "Dendro"])
        
        return PersonajeGacha(nombre, rareza_elegida, elemento)

def main():
    for _ in range(5):
        personaje = PersonajeGacha.invocar()
        print(personaje)

if __name__ == "__main__":
    main()
