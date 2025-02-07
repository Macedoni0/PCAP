import random

class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
    
    def atacar(self, otro_personaje):
        if otro_personaje.vida <= 0:
            raise ValueError(f"{otro_personaje.nombre} ya está derrotado!")
        
        if not otro_personaje.esquivar():
            otro_personaje.vida -= self.ataque
            otro_personaje.vida = max(0, otro_personaje.vida)
            print(f"Vida restante: {otro_personaje.vida}")
        else:
            print(f"{otro_personaje.nombre} esquivo el ataque de {self.nombre}!")
    
    def esquivar(self):
        return random.random() < 0.3 
    
heroe = Personaje("Héroe", 100, 20)
enemigo = Personaje("Enemigo", 80, 15)

heroe.atacar(enemigo)
enemigo.atacar(heroe)
heroe.atacar(enemigo)
heroe.atacar(enemigo)