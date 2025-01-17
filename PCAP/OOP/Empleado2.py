class Empleado:
    plantilla=[]
    num_empleado=0

    def __init__(self, nombre: str, cargo, salario=25000.50):
        self.nombre = nombre
        self.cargo = cargo
        self.__salario = salario
        Empleado.plantilla.append(self)
        Empleado.num_empleaods=+1

    def get_salario(self):
        return self.__salario
    def __repr__(self):
        return f"Empleado('{self.nombre}', '{self.cargo}', {self.get_salario()})"

    
empleado1 = Empleado("Juanma","Director", 75000.0),
empleado2 = Empleado("Teresa","Presidenta", 80000.0),
empleado3 = Empleado("Ana","Administrativa", 2500.0),
empleado4 = Empleado("Mario","Conserje", 20000.0),
empleado5 = Empleado("Aitor","Desarrollador", 50000.0)

for empleado in Empleado.plantilla:
    print(empleado)