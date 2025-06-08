class Empleado:
    def __init__(self,nombre:str, edad:int, salario:float):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    def __str__(self):
        return f"Empleado[ empleado={self.nombre}, edad={self.edad}, salario={self.salario} ]"