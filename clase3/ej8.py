## 8-Crear una lista con los números del 1 al 10 y mostrarlos en orden inverso.
numero = [1,2,3,4,5,6,7,8,9,10]
numero_inverso = numero[::-1]
numero_inverso = numero[-5:-1] ## trae desde el 6 hasta el 9

print(numero_inverso)

numeros = list(range(1, 11))
numeros.reverse()
print(numeros)