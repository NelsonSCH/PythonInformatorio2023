## 18-Crea un programa que pida al usuario su nombre, su edad y su ciudad de residencia, y lo muestre en pantalla Utilizando una sola línea de código. *Recuerda el print() del ejercicio anterior 

nombre = input("Ingrese su nombre : ")

edad = int(input("Ingrese su edad : "))

ciudad = input("Ingrese su ciudad de residencia actual : ")

print(
    f"""
El usuario:{nombre}
Su edad es: {edad}
Actualmente esta en la ciudad: {ciudad}
"""
)
