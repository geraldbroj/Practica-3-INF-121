import pickle

class Medicamento:
    def __init__(self, nombre, codMedicamento, tipo, precio):
        self.nombre = nombre
        self.codMedicamento = codMedicamento
        self.tipo = tipo
        self.precio = precio
    def mostrar(self):
        print(f"{self.nombre} | {self.tipo} | {self.precio}")

    def getTipo(self):
        return self.tipo

    def getPrecio(self):
        return self.precio


class Farmacia:
    def __init__(self, nombreFarmacia, sucursal, direccion, medicamentos=[]):
        self.nombreFarmacia = nombreFarmacia
        self.sucursal = sucursal
        self.direccion = direccion
        self.medicamentos = medicamentos
    def mostrar(self):
        print(f"{self.nombreFarmacia} - Sucursal: {self.sucursal} - Dirección: {self.direccion}")
        for m in self.medicamentos:
            m.mostrar()
    def getDireccion(self):
        return self.direccion

    def getSucursal(self):
        return self.sucursal
    
    def buscaMedicamento(self, x):
        for m in self.medicamentos:
            if m.nombre.lower()== x.lower():
                return True
        return False
    
    def mostrarMedicamentos(self, tipo):
        for m in self.medicamentos:
            if m.tipo.lower() == tipo.lower():
                m.mostrar()

class ArchFarmacia:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
    
    def crearArchivo(self, farmacia):
        with open(self.nombre_archivo, 'wb') as f:
            pickle.dump([],f)

    def adicionar(self, farmacia):
        farmacias = self.leer()
        farmacias.append(farmacia)
        with open(self.nombre_archivo, 'wb') as f:
            pickle.dump(farmacias, f)
    
    def leer(self):
        with open(self.nombre_archivo, 'rb') as f:
            return pickle.load(f)
    def listar(self):
        for f in self.leer():
            f.mostrar()
    def mostrarMedicamentosResfrios(self):
        for f in self.leer():
            f.mostrarMedicamentos("resfrio")
    
    def precioMedicamentoTos(self):
        total = 0
        for f in self.leer():
            for m in f.medicamentos:
                if m.tipo.lower() == "tos":
                    total += m.precio
        return total  

    
    def mostrarMedicamentosMenorTos(self):
        for f in self.leer():
            for m in f.medicamentos:
                if m.tipo.lower() == "tos" and m.precio < 10:
                    m.mostrar()

    def mostrarMedicamentosSucursalTos(self, sucursal):
        for f in self.leer():
            if f.getSucursal() == sucursal:
                f.mostrarMedicamentos("tos")

    def buscarSucursalConMedicamento(self, nombre_medicamento):
        for f in self.leer():
            if f.buscaMedicamento(nombre_medicamento):
                print(f"Sucursal: {f.getSucursal()} | Dirección: {f.getDireccion()}")

arch = ArchFarmacia("farmacias.dat")
arch.crearArchivo()

meds1 = [Medicamento("Golpex", 1, "Tos", 12.5), Medicamento("Resfrix", 2, "Resfrio", 9.0)]
meds2 = [Medicamento("Bronquix", 3, "Tos", 8.0), Medicamento("Paracetamol", 4, "Fiebre", 7.0)]

f1 = Farmacia("Salud Total", 101, "Calle 1, Zona Central", meds1)
f2 = Farmacia("Farmacia Plus", 202, "Av. Siempre Viva 742", meds2)

arch.adicionar(f1)
arch.adicionar(f2)

print("--- Listar todas las farmacias ---")
arch.listar()

print("\n--- Medicamentos para resfríos ---")
arch.mostrarMedicamentosResfrios()

print("\n--- Precio total medicamentos para la tos ---")
print(arch.precioMedicamentoTos())

print("\n--- Medicamentos para la tos con precio < 10 ---")
arch.mostrarMedicamentosMenorTos()

print("\n--- Medicamentos para la tos en sucursal 202 ---")
arch.mostrarMedicamentosSucursalTos(202)

print("\n--- Buscar sucursales con medicamento 'Golpex' ---")
arch.buscarSucursalConMedicamento("Golpex")