from Formulas import area_triangulo, area_cuadrado

# Usamos las funciones del archivo "formulas.py"
print(area_triangulo(5, 10))   # Salida: 25.0
print(area_cuadrado(4))  # Salida: 16

#Ventajas de estructurar el código así:
#✅ Código más limpio: Separamos funciones reutilizables en otro archivo.
#✅ Reutilización: Podemos importar formulas.py en otros programas.
#✅ Modularidad: Podemos agregar más funciones sin modificar guia.py.