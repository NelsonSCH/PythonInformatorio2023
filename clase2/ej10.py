## 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es una vocal o una consonante.

letra = str(input("Ingrese una letra: ")).lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"La letra {letra} es una vocal")
else:
    print(f"La letra {letra} ingresa es una consonante")
    
   
## Otro metodo
    
#letra = input("Ingresar una letra: ").lower()
#vocales = "aeiou"
#if vocales.find(letra) > 0:
 #   print(f"{letra} es una vocal")
#else:
#    print(f"{letra} es una consonante")