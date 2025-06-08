from typing import Generic, TypeVar

T = TypeVar('T')

class Caja(Generic[T]):
    def __init__(self):
        self.cont: T = None
    def guardar(self,cont: T):
        self.cont = cont
    def obtener(self)-> T:
        return self.cont

caja_txt = Caja[str]()
caja_txt.guardar("holaaaa")
caja_numero = Caja[int]()
caja_numero.guardar(2567)

print("Contenido de caja texto: ", caja_txt.obtener())
print("contenido de caja numero", caja_numero.obtener())