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

#Tuplas son parecidas a las listas pero son inmutables

mi_tupla= (1,2,3,4)
print (mi_tupla[3])
#Tuplas son inmutables, no se pueden modificar


#Sets: es util para eliminar elementos duplicados de una lista

my_set = set([1,2,3,4,4,4])
print(my_set)
