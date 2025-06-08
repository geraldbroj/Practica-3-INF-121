from typing import Generic, TypeVar, List

T = TypeVar('T')

class Catalogo(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []
    
    def agregar(self,elemento: T):
        self.elementos.append(elemento)

    def buscar(self, crit) -> List[T]:
        return[e for e in self.elementos if crit(e)]
    
#b)
class Libro:
    def __init__(self,titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def __str__(self):
        return f"{self.titulo} por {self.autor}"
    
cat_libro = Catalogo[Libro]()
cat_libro.agregar(Libro("Cien años de soledad", "Gabriel García Márquez"))
cat_libro.agregar(Libro("Don Quijote de la Mancha", "Miguel de Cervantes"))
# Buscar por autor
libros_cervantes = cat_libro.buscar(lambda l: "Cervantes" in l.autor)
print("Libros de Cervantes:")
for libro in libros_cervantes:
    print(libro)

class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

cata_prod = Catalogo[Producto]()
cata_prod.agregar(Producto("Laptop", 1200))
cata_prod.agregar(Producto("Smartphone", 800))

prod_caros = cata_prod.buscar(lambda p:p.precio > 1000)
print("Productos caros:")
for producto in prod_caros:
    print(producto)
