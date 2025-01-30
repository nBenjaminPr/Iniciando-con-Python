#Numpy array: son estruturas eficientes de listas y diccionarios para manejar grandes cantidades datos numericos, enteros y fraccionarios y flotantes. 
#Para usar **NumPy** y **arrays** en Python, primero debes asegurarte de tener **NumPy** instalado en tu entorno de Python.
# Puedes instalarlo usando un administrador de paquetes de Python como **pip**: ```pip install numpy```


import numpy as np

lista = [0,1,2,3,4,5]
my_array = np.array(lista)
print(my_array) # [0 1 2 3 4 5]

lista1 = [1,2,3]
lista2 = [10,20,30]
lista3 = [100, 200, 300]

array1 = np.array(lista1)
array2 = np.array(lista2)
array3 = np.array(lista3)

print (lista1 + lista2 + lista3)

print(array1 + array2 + array3)