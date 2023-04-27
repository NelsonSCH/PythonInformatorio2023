##9-Escribe un programa que solicite al usuario dos números y luego imprima la suma, la resta, la multiplicación y la división de los dos números.
# variables

num1 = int(input("Ingrese el primer numero: "))

num2 = int(input("Ingrese el segundo numero: "))

# Operaciones

suma = num1 + num2

resta = num1 - num2

division = num1 // num2

multiplicacion = num1  * num2


# Impresion

print(
f"""
Los resultados de las operaciones son las siguietes
La suma es {suma}
La resta es {resta}
La multiplicacion es {multiplicacion}
la division es {division}
"""
)


