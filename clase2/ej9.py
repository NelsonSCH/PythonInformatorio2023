## 9-Escribir un programa que pida al usuario tres números y muestre por pantalla el mayor de ellos.

numero_1  = int(input("Ingrese el primer valor: "))
numero_2 = int(input("Ingrese el segundo valor: "))
numero_3 = int(input("Ingrese el tercer valor: "))

if numero_1 > numero_2 and numero_1 > numero_3 :
    print(f"El mayor es {numero_1} ")
elif numero_1 < numero_2 and numero_2 > numero_3:
    print(f"El mayor es {numero_2} ")
    
else:
    print(f"El mayor es {numero_3} ")
    