## 14-Escribe un programa que solicite al usuario un número entero y luego imprima el doble y el triple de ese número.

numero = int(input("Ingrese un número entero: "))

doble = numero * 2
triple = numero * 3

print(f"""
Numero ingresado : {numero}
El doble del numero ingresado es : {doble}
El triple del numero ingresado es : {triple}
""")
