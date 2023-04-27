## 17-Escribe un programa que solicite al usuario dos palabras y luego las imprima en orden inverso. Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir "mundo hola". Importante!!! Utiliza un solo print() 😈.

palabra1 = input(
    "Ingrese la primer palabra : "
)

palabra2 = input("Ingrese la segunda palabra : ")

ordenada = palabra1 + " " + palabra2

invertida = palabra2 + " " + palabra1

print(f"""
Palabras ordenadas por orden de ingreso : {ordenada}
Palabras impresas de forma inversa a su forma de ingreso : {invertida}
"""
)
