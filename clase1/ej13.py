## 13-Escribe un programa que solicite al usuario su nombre y su edad, y luego imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

edad_futura = edad + 10

print(
    f""" Dentro de 10 años {nombre} tendrá {edad_futura}  años de edad"""
)
