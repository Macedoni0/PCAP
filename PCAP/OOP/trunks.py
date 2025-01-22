class Humano:
    origen = 'La Tierra'
    def __init__(self, nombre):
        self.nombre = nombre

class Saiyan:
    origen = 'Sadala'
    def __init__(self, nombre):
        self.nombre = nombre

class Mestizo(Saiyan, Humano):
    def __init__(self, a, b, nombre):
        self.nombre = nombre
        self.padre = a.nombre
        self.madre = b.nombre
    
    def verAncestros(self):
        for x in Mestizo.__bases__:
            print(x.__name__, end=' ')
        print()

goku = Saiyan("Son Goku")
vegeta = Saiyan("Vegeta")
bulma = Humano("Bulma")
trunks = Mestizo(vegeta, bulma, "Trunks")

print(f"El padre de {trunks.nombre} es {trunks.padre}")
print(f"El origen de {trunks.nombre} es {trunks.origen}") 
print(f"la madre de {trunks.nombre} es {trunks.madre}")
 
Saiyan.origen = "Tierra" 
print(f"Trunks es de {trunks.origen}")
print(f"Goku es de {goku.origen}")

if type(trunks).__name__ == "Mestizo":
    if issubclass(Mestizo, Saiyan):
        print(f"{trunks.nombre} puede convertirse en super saiyan")
        if issubclass(Mestizo, Humano):
            print(f"{trunks.nombre} tiene madre humana")
    else:
        print(f"{trunks.nombre} no puede convertirse en super saiyan")
