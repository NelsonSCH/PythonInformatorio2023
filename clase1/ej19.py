## 19-Escribe un programa que solicite al usuario un número decimal y luego imprima la parte entera y decimal por separado.

numero = float(input("Ingrese un número decimal: "))

parte_entera = int(numero)

parte_decimal = numero - parte_entera

print(
    f"""
Numero ingresado en decimales: {numero}
Parte entera del numero ingresado: {parte_entera}
Parte decimal del numero ingresado: {parte_decimal}
"""
)
