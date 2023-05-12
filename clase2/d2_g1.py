print("*********************************************************")
print("********** Bienvenidos al Analizador de textos G1 **********")
print("*********************************************************\n")
print("A continuación, por favor ingrese un texto o una frase que prefiera.\n")


texto = str (input("Ingrese el texto aquí: ")).lower()  #convertir texto en minuscula

print("Gracias. Ahora por favor ingrese 3 letras a elección...")


letra1 = str(input("Ingrese una letra aquí: ")).lower()
letra2 = str(input("Ingrese la segunda letra: ")).lower()
letra3 = str(input("Ingrese la tercer letra: ")).lower()


# consigna 1: contar las letras que se repiten en el texto
cantidad_letra1= (texto.count(letra1))
cantidad_letra2= (texto.count(letra2))
cantidad_letra3= (texto.count(letra3))
print("__________________________________________________________\n")


print(f"La letra '{letra1}' se repite: {cantidad_letra1} veces \n"
      f"La letra '{letra2}' se repite: {cantidad_letra2}  veces \n"
      f"La letra '{letra3}' se repite:  {cantidad_letra3} veces"
      )

print("__________________________________________________________\n")
# Consigna 2: cuantas palabras hay en el texto

texto_lista = texto.split(' ') #convertir texto en lista, separado por un espacio en blanco
cantidad_palabras= (len(texto_lista)) # usar len para contar la cantidad de palabras
print("Hay", cantidad_palabras, "palabras en el texto")

print("__________________________________________________________\n")

# Consigna 3: Cual es la primera letra y cuál es la última. (Indexación) 
print ("Primer letra del texto: ", texto[0], "\n"
       "Ultima letra: ", texto[-1])
print("__________________________________________________________\n")

# Consigna 4: Mostrar el texto en orden inverso.
inverso = texto[len(texto)::-1]
print("El inverso del texto es: ", inverso)
print("__________________________________________________________\n")

# Consigna 5: Decir si la palabra "python" aparece en el texto.
if "python" in texto.lower():
    print("La palabra 'python' aparece en el texto.")
else:
    print("La palabra 'python' no aparece en el texto.")
    
print("__________________________________________________________\n")

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
