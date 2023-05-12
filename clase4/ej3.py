numero = int(input("Ingrese un numero: "))
print(f"\n\nA continuacion te presento la tabla de multiplicar del numero {numero}:\n")

for mult in range(1,11):
    print(f"{numero}x{mult}={numero*mult}")