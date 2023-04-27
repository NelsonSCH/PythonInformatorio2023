## 12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato dd/mm/aaaa y luego imprima su edad en años. Utiliza la función .split()

fecha = input("Ingrese su fecha de nacimiento con el formato dd/mm/aa : ")

fecha_tranformada = fecha.split("/")

edad = 2023 - int(fecha_tranformada[2])


print("La fecha ingresada es : ", edad)
