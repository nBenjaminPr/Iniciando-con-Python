#En los casos anteriores, la última instrucción de nuestras funciones ha sido imprimir un resultado. Esto puede resultarnos útil para ver ese resultado, pero no nos permite guardar este valor. Una alternativa a esto es definir un **retorno** para nuestra función, es decir, lo que queremos que retorne para almacenarlo, por ejemplo, en una variable. Por ejemplo,modificaremos la función anterior: 

def promedio_lista(lista):
    suma=0
    for i in lista:
        suma = suma + i
    promedio = round(suma/len(lista),1)
    return(promedio)


a = promedio_lista([5,4.7,6.5])
b = promedio_lista([5.5,6.2,4.5])

c = a + b
print(a)
print(b)
print(c)


def promedio_lista2(lista2):
    suma=0
    for i in lista2:
        suma = suma + i
    promedio2 = round(suma/len(lista2),1)

    if promedio2 >= 4:
        resultado = 'aprobado'
    else:
        resultado = 'reprobado'
    return(promedio2, resultado)

print(promedio_lista2([5,4.7,6.5]))
print(promedio_lista2([5,4.7,6.5])[1]) #En la segunda línea, [1] accede solo al estado "Aprobado". 🚀



