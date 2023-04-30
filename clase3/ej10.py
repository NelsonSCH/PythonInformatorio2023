## 10-Crear una lista con los nombres de tres frutas y eliminar la segunda fruta de la lista. Mostrar la lista resultante.

from os import remove


frutas = ["pera", "manzana", "naranja"]
frutas.remove("manzana")
print(frutas)