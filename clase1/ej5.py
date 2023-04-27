## 5-Crea un programa que pida al usuario dos números enteros y muestre en pantalla su cociente y su resto.

n1 = int(input("Ingrese el primer valor: "))

n2 = int (input("Ingrese el segundo valor: "))
cociente = (n1 / n2)
print("El resultado del cociente es:", cociente)
resto = (n1 % n2)
print("Su resto es:", resto)


## Otro metodo

res = divmod(n1, n2)
print("El resultado del cociente y resto es:", res)