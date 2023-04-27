## 6-Crea un programa que pida al usuario el radio de un círculo y calcule su área. La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado. Supongamos que pi = 3.1416

pi = float("3.1416")

r =  float (input('Escriba el radio del circulo: '))

a = (pi * (r ** 2))
print('El area del circulo es: {}'.format(a))
