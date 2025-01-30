#Para transformar listas a diccionarios se usa la funcion zip()

nombre =["Juan","Pedro","Lucas"]
edad = [28,30,25]

diccionario_edad = dict(zip(nombre,edad))

print(diccionario_edad)

#Diccionario a listas

diccionario_edades = {'Juan': 28, 'Pedro': 30, 'Lucas': 25}

nombres = list(diccionario_edades.keys())
edades = list(diccionario_edades.values())

print (nombres)
print (edades)