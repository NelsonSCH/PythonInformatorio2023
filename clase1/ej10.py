##10-Crea un programa que pida al usuario una cantidad en dólares y la convierta a euros. Supón que el tipo de cambio es de 0.84 euros por dólar.

tipo_cambio = 0.84

cantidad_dolares = float(input( "Ingrese la cantidad de dolares : "))

cambio = tipo_cambio * cantidad_dolares

print(
    f"""El cambio de dolar a euros es:
Dolar - USD${cantidad_dolares}
Euros - EU${cambio}
"""
)
