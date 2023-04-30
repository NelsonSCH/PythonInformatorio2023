## 6-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es múltiplo de 2 y de 3 a la vez.

numero = int(input("Ingrese un numero entero: "))

if numero % 2 == 0:
    print(numero, "es multiplo de 2")
elif numero % 3 == 0:
    print(numero, "es multiple de 3")
else :
    print("no son multiples de 2 y 3")