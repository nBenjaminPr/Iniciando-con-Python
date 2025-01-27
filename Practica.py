#Ejercicio
"""
Crearemos ahora un programa que solicita al usuario:

*   El precio de un artículo
*   La cantidad de ellos que comprará
*   El porcentaje de descuento que se ofrece para ese artículo

Hecho esto, nos retornará el valor total a pagar, de la forma "El total a pagar es de ... pesos"

"""

    # Solicitar al usuario el precio del artículo
precio_articulo = float(input("Ingrese el precio del artículo: "))

    # Solicitar al usuario la cantidad de artículos que comprará
cantidad_articulos = int(input("Ingrese la cantidad de artículos que comprará: "))

    # Solicitar al usuario el porcentaje de descuento
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento ofrecido: "))

    # Calcular el total a pagar con el descuento
descuento = precio_articulo * (porcentaje_descuento / 100)
total_pagar = (precio_articulo - descuento) * cantidad_articulos

    # Mostrar el resultado
print(f"El total a pagar es de {total_pagar:.2f} pesos")