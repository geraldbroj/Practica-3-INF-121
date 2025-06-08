from typing import Generic, TypeVar, List

T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []
    
    def apilar(self, elemento: T):
        self.elementos.append(elemento)

    def desapilar(self) -> T:
        if self.elementos:
            return self.elementos.pop()
        else:
            raise IndexError("Pila Vacia")
    def mostrar(self):
        return self.elementos[::-1]

pila_num = Pila[int]()
pila_num.apilar(1)
pila_num.apilar(2)
print("Pila de numeros:", pila_num.mostrar())
print("Desapilado", pila_num.desapilar())

pila_txt= Pila[str]()
pila_txt.apilar("ho")
pila_txt.apilar("so")
print("Pila de texto:", pila_txt.mostrar())
print("Desapilado:", pila_txt.desapilar())
pila_bool = Pila[bool]()
pila_bool.apilar(True)
pila_bool.apilar(False)
print("Pila de booleanos:", pila_bool.mostrar())