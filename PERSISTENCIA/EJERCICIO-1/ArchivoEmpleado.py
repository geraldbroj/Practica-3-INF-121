import pickle
import os
from Empleado import Empleado

class ArchivoEmpleado:
    def __init__(self, nomA: str):
        self.nomA = nomA

    def crearArchivo(self):
        with open(self.nomA, "wb") as archivo:
            pickle.dump([],archivo)
    
    def guardarEmpleado(self, e: Empleado):
        empleados = []
        if os.path.exists(self.nomA):
            with open(self.nomA, "rb") as archivo:
                empleados = pickle.load(archivo)
        empleados.append(e)
        with open(self.nomA, "wb") as archivo:
            pickle.dump(empleados,archivo)

    def buscaEmpleado(self, nombre: str):
        if os.path.exists(self.nomA):
            with open(self.nomA, "rb") as archivo:
                empleados = pickle.load(archivo)
                for e in empleados:
                    if e.nombre == nombre:
                        return e
        return None

    def mayorSalario(self, sueldo: float):
        if os.path.exists(self.nomA):
            with open(self.nomA, "rb") as archivo:
                empleados = pickle.load(archivo)
                for e in empleados:
                    if e.salario > sueldo:
                        return e
        return None
    

archivo = ArchivoEmpleado("empleados.dat")
archivo.crearArchivo()
archivo.guardarEmpleado(Empleado("Ana", 30, 3500.0))
archivo.guardarEmpleado(Empleado("Luis", 25, 4200.0))

print("Buscando Ana:")
print(archivo.buscaEmpleado("Ana"))

print("Buscando con salario mayor a 4000:")
print(archivo.mayorSalario(4000))