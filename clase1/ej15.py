## 15-Escribe un programa que solicite al usuario una temperatura en grados Celsius y luego imprima la temperatura equivalente en grados Fahrenheit. La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.

celsius = float(input("Ingrese una temperatura en grados Celsius: "))

fahrenheit = (celsius * 1.8) + 32

print(celsius, "grados Celsius equivalen a", fahrenheit, "grados Fahrenheit.")
print(f""" Grados celsius ingresados : {celsius} Grados fahrenheit : {fahrenheit} """)
