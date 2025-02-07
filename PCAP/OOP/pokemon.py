class Pokemon:
    def __init__(self, nombre, tipo, vida, ataque):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
    
    def atacar(self, otro_pokemon):
        if otro_pokemon.vida <= 0:
            raise ValueError("Este Pokémon ya está derrotado")
        
        otro_pokemon.vida -= self.ataque
        if otro_pokemon.vida < 0:
            otro_pokemon.vida = 0
        
        print(f"Vida restante de {otro_pokemon.nombre}: {otro_pokemon.vida}")

pikachu= Pokemon("Pikachu", "eléctrico", 100,20)
charmander = Pokemon("Charmander", "fuego", 80, 25)
    
pikachu.atacar(charmander)
charmander.atacar(pikachu)
pikachu.atacar(charmander)
pikachu.atacar(charmander)






