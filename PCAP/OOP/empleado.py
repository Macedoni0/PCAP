class Empleado:
    def __init__(self, nombre, edad, salario=1000):
        self.nombre = nombre
        self.edad = edad
        self.__salario = salario

    def getSalario(self):
        return self.__salario

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.getSalario()}"

listaEmpleados = [
    Empleado("Juan", 30, 75000.0),
    Empleado("Ana", 25, 80000.0),
    Empleado("Luis", 40, 20000.0)
]

#for empleado in listaEmpleados:
# print(empleado)

empleados_vip = [empleado for empleado in listaEmpleados
                 if empleado.getSalario() > 50000]
for e in empleados_vip:
    print(e)