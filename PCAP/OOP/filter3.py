'''
    Ejercicio de clase.
    Crear una clase Empleado que modele trabajadores con un nombre y apellidos, un cargo y un salario.
    El salario debe ser (obligatoriamente) un atributo privado.
'''
class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.__salario = salario  # Atributo privado
    def get_salario(self):
        return self.__salario
    def __str__(self):
        return f"{self.nombre} - {self.cargo} - Salario: {self.__salario}€"
listaEmpleados = [
    Empleado("Juanma", "Director", 75000),
    Empleado("Teresa", "Presidenta", 80000),
    Empleado("Ana", "Administrativo", 25000),
    Empleado("Mario", "Conserje", 20000)
]
# Seleccionar los empleados cuyo salario sea > 50k al año
empleados_vip = list(filter(lambda e: e.get_salario() > 50000, listaEmpleados))
# Mostrar empleados VIP
for ev in empleados_vip:
    print(ev)
print("Alvaro Avila Martinez")
