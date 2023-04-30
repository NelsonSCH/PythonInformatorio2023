##  4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por pantalla si está aprobado (5 o más) o no.

nota = float(input("Ingrese una nota: "))

if nota >= 6 and nota <=10:
    print("Aprobado")
elif nota >= 0 and nota <=5:
    print("Desaprobado")
else: 
    print("No corresponde a una nota estándar")
    