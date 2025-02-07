class CartaNoEncontradaError(Exception):
    pass

class Carta:
    def __init__(self, nombre, ataque, defensa, tipo):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.tipo = tipo
    
    def __str__(self):
        return f"{self.nombre} | ATK: {self.ataque} | DEF: {self.defensa} | Tipo: {self.tipo}"

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mazo = []
        self.campo = []
    
    def agregar_carta(self, carta):
        self.mazo.append(carta)
        print(f"{carta.nombre} ha sido añadida al mazo de {self.nombre}")
    
    def invocar_carta(self, nombre):
        for carta in self.mazo:
            if carta.nombre == nombre:
                self.campo.append(carta)
                self.mazo.remove(carta)
                print(f"ha invocado {carta.nombre}")
                return
        raise CartaNoEncontradaError(f"La carta no esta en el mazo")
    
    def mostrar_mazo(self):
        print(f"Mazo de {self.nombre}:")
        for carta in self.mazo:
            print(f"- {carta}")
    
    def mostrar_campo(self):
        print(f"Cartas en el campo de {self.nombre}:")
        for carta in self.campo:
            print(carta)


dragon_blanco = Carta("Dragón Blanco de Ojos Azules", 3000, 2500, "Dragón")
mago_oscuro = Carta("Mago Oscuro", 2500, 2100, "Mago")
jugador = Jugador("Yugi")
    
jugador.agregar_carta(dragon_blanco)
jugador.agregar_carta(mago_oscuro)
    
jugador.mostrar_mazo()
    
jugador.invocar_carta("Mago Oscuro")
jugador.mostrar_campo()
jugador.invocar_carta("Exodia") 
