import pickle
import os


class Cliente:
    def __init__(self, id,nombre,telefono):
        self.__id=id
        self.__nombre = nombre
        self.__telefono = telefono

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def telefono(self):
        return self.__telefono
    def __str__(self):
        return f"Cliente(id={self.__id}, nombre='{self.__nombre}', telefono={self.__telefono})"

class ArchivoCliente:
    def __init__(self, nombre_archivo):
        self.__nomA = nombre_archivo
    
    def crear_archivo(self):
        with open(self.__nomA, 'wb') as archivo:
            pickle.dump([],archivo)
        
    def guardar_cliente(self,cliente):
        clientes = self._leer_clientes()
        clientes.append(cliente)
        self._escribir_clientes(clientes)
    
    def buscar_cliente(self, id):
        for cliente in self._leer_clientes():
            if cliente.id == id:
                return cliente
        return None
    
    def buscar_celular_cliente(self, telefono):
        for cliente in self._leer_clientes():
            if cliente.telefono == telefono:
                return cliente
        return None
    
    def _leer_clientes(self):
        if not os.path.exists(self.__nomA):
            return []
        with open(self.__nomA, 'rb') as archivo:
            return pickle.load(archivo)
    
    def _escribir_clientes(self, clientes):
        with open(self.__nomA, 'wb') as archivo:
            pickle.dump(clientes, archivo)

archivo = ArchivoCliente("clientes.dat")

archivo.crear_archivo()

archivo.guardar_cliente(Cliente(1, "Juan", 123456))
archivo.guardar_cliente(Cliente(2, "Ana", 987654))

c1 = archivo.buscar_cliente(1)
print("Buscar por ID:", c1 if c1 else "No encontrado")

c2 = archivo.buscar_celular_cliente(987654)
print("Buscar por celular:", c2 if c2 else "No encontrado")