##Se te pide crear un programa que le pida al usuario que ingresar un texto cualquiera,
# por ejemplo, un artículo o una frase. Luego el programa le va a pedir al usuario que también ingrese 3 letras a su elección.
# Nuestro código va a procesar esa información para realizar los análisis necesarios para devolverle al usuario la siguiente información:
	
import msvcrt
import os

print("*********************************************************")
print("********** Bienvenidos al Analizador de textos **********")
print("*********************************************************\n")
print("A continuación, ingrese un texto o una frase que prefiera.\n")

texto = [(input("Ingrese el texto aquí: "))]
os.system ("cls")
print("Gracias. Ahora por favor ingrese 3 letras a elección...\n")
letra =[(input("Ingrese las letras aquí: "))]

print("Aguarde, estamos procesando tu información....")






contiene_python = 'python' in texto.lower()
mensaje_que_contiene_python = {True: "La palabra 'python' aparece en el texto", False: "La palabra 'python' no aparece en el texto"}

##print(f"ingresaste: {texto}")
print("Presione una tecla para finalizar...")
msvcrt.getch()