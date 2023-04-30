## 5-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("Ingrese un numero entero: "))

if numero % 2 == 0:
    print(numero, "es un número par")
else:
    print(numero, "es un número impar")