import random


nombre = str(input("Hola por favor ingrese su nombre: "))
print("=====================================================")
print(f"Bienvenido {nombre} al juego 'ADIVINA EL NÚMERO'\n")
print("Reglas del juego: \n"
      "a) El usuario debera ingresar un numero entero.\n"
      "b) Debera adivinar el número entre 1 al 100.\n"
      "c) Tendra solo 8 intentos para adivinar el número.")
print("=====================================================")

print(" Buena Suerte!!!")
intentos = 0
numero_rand = random.randint(1,100)
print(numero_rand) #TESTER DEL Numero random  "LUEGO SE LO ELIMINA"
while(intentos < 8):
    numero = (input("Ingrese el numero aquí: "))
    if numero.isdigit():
        numero = int(numero)
        intentos =  intentos + 1
        if numero < numero_rand and intentos < 8:
            print(f"El numero a adivinar es mayor, intentos restantes: {8 - intentos}")
        elif numero > numero_rand and intentos <8:
            print(f"EL numero a adivinar es menor, intentos restantes: {8 - intentos}")
        elif numero == numero_rand:
            print(f"Felicidades {nombre} has adivinado el numero '{numero_rand}' en solo {intentos} intentos!!!")
            break
        else:
            print(f"Game Over, superaste los intentos fallidos!!!. El número a divinar era: '{numero_rand}'")
    else: 
        print("Has ingresado una letra o un numero decimal .Por favor ingresa un numero entero!!!")
    
    
    # GRUPO 1
    # Suarez German Daniel
    # Schaab Medina Nelson
    # Abson Lucas Bautista
    # Durnbeck Federico
    # Landriel Lautaro
    # Giroldi Lucas Ezequiel
    # Sanso Pedro
    # Zabala Villalba Daiana Jacqueline
    # Nuñez Juan
    # Neumann Lucas
    # Barboza Lucas David