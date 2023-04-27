## 8-Crea un programa que pida al usuario el radio de un círculo y muestre su diámetro, su circunferencia y su área. Supón que pi es aproximadamente 3.14159.

radio = float(input("Ingrese el radio del circulo : " ))

pi = 3.1416

diametro = 2 * radio

circunferencia = 2 * pi * radio

area = pi * (radio ** 2)

print("El diametro del circulo es : ", diametro)

print("La circunferencia del circulo es : ", circunferencia
)

print("El area del circulo es ", area
)

