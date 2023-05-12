# DICCIONARIO { }
diccionario = {"Nelson": "Castelli", "Cristian": "SP", "Ramiro": "Resis"}
# clave = unica   |   valor = cualquier tipo de dato

#imprimir el valor de una clave
print(diccionario["Nelson"])

#cambiar valor de una clave
diccionario["Nelson"] = 24

print(diccionario.keys())

print(diccionario.values())

print(diccionario.items())

#elimina el ultimo item
diccionario.popitem()
print(diccionario)

#elimina un item en especifico
diccionario.pop("Nelson")
print(diccionario)