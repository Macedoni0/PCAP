class InventarioLlenoError(Exception):
    pass

class Item:
    def __init__(self, nombre, tipo, rareza):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza

    def __str__(self):
        return f"{self.nombre} ({self.tipo}, {self.rareza})"

class Personaje:
    MAX_ITEMS = 5
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []
    
    def agregar_item(self, item):
        if len(self.inventario) >= self.MAX_ITEMS:
            raise InventarioLlenoError("El inventario esta lleno")
        self.inventario.append(item)
        print(f"{item.nombre} ha sido agregado al inventario de {self.nombre}")
    
    def eliminar_item(self, item_nombre):
        for item in self.inventario:
            if item.nombre == item_nombre:
                self.inventario.remove(item)
                print(f"{item.nombre} ha sido eliminado del inventario de {self.nombre}")
                return
        print("El objeto no esta en el inventario")
    
    def mostrar_inventario(self):
        if not self.inventario:
            print("El inventario esta vacio")
        else:
            print(f"Inventario de {self.nombre}:")
            for item in self.inventario:
                print(item)

jugador= Personaje("Guerrero")
espada = Item("Espada legendaria", "Arma", "Epico")
jugador.agregar_item(espada)

jugador.agregar_item(espada)
jugador.agregar_item(espada)
jugador.agregar_item(espada)
jugador.agregar_item(espada)
jugador.agregar_item(espada)