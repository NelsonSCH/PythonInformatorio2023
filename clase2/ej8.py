## 8-Escribir un programa que pida al usuario una cadena de caracteres y muestre por pantalla si contiene la letra "a".

palabra = str(input("Ingrese una palabra: ")).lower()

if "a" in  palabra :
    print(f"La palabra {palabra}:  contiene la letra 'a' ")
else:
    print(f"La palabra {palabra}:  no contiene la letra 'a' ")
    