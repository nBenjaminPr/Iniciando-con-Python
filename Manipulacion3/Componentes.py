#Python cuenta con funciones ya definidas -conocidas como **built-in functions**, que memos utilizado durante este módulo como **print**, **input**, etc. Veremos ahora cómo podemos definir una función nosotros mismos (**user defined functions**) para realizar más fácilmente las tareas que deseemos.

#Supongamos que en un curso se realizan 3 pruebas y 5 tareas, además de un examen final. La nota de cada estudiante se calcula considerando que:

#- El promedio de las pruebas corresponde al 50% de la nota final
#- El promedio de las tareas corresponde al 30% de la nota final
#- El examen corresponde al 20% de la nota final.

#La nota de cada estudiante depende, en total, de 12 valores: las 9 notas y los tres porcentajes o ponderaciones dadas. Si queremos establecer una fórmula que calcule la nota final tendremos que considerar estos 12 valores o **parámetros**. Pero ya que consideramos los porcentajes como valores fijos (aunque podrían modificarse), las notas obtenidas corresponderán a los **argumentos** de nuestra función, es decir, los valores que recibiremos de un usuario para realizar nuestros cálculos.

def nota_final(prueba1,prueba2,prueba3,tarea1,tarea2,tarea3,tarea4,tarea5,examen):
    promedio_pruebas=round((prueba1+prueba2+prueba3)/3,1)
    promedio_tareas=round((tarea1+tarea2+tarea3+tarea4+tarea5)/5,1)
    final=round(0.5*promedio_pruebas+0.3*promedio_tareas+0.2*examen,1)
    
    print(final)

nota_final(5,4.2,5,4,5,4,7,4,4)
    #Podemos observar que:
#- Utilizamos la palabra reservada **def** para señalar que estamos definiendo una función.
#- Luego viene el nombre de la función, en nuestro caso **nota_final**. Aunque podŕiamos ponerle cualquier nombre, es una buena práctica llamarla de una manera intuitiva, que se relacione con lo que realiza. Si utilizamos más de una palabra, se utiliza el guión bajo para unirlas, y siempre con minúsculas. Esto se conoce como **snake case**, y es un formato establecido para la creación de funciones en Python.
#- Junto al nombre de la función, entre paréntesis, escribimos todos sus argumentos, y finalizamos con **:**.
#- Luego de los **:**, si presionamos **enter**, el bloque de código estará con indentación, para delimitar que esto corresponde a la definición o **cuerpo** de la función. Aquí escribimos tomas las instrucciones que queremos que nuestra función ejecute.


""""Parametro """
#Es posible definir, de todos modos, funciones **sin argumentos**, que en cada ocasión realizarán lo mismo. Esto puede ser muy útil si, por ejemplo, hay un texto que se debe repetir muchas veces y no queremos copiarlo y pegarlo en cada ocasión, arriesgándonos a cometer errores. Por ejemplo:

"""def saludo():
    print('Muy buenos días, amables estudiantes')"""

def saludo():
    nombre = input('¿Cuál es su nombre? ')
    print(f'Muy buenos días, {nombre}')

saludo()


#Python nos permite utilizar, además, diferentes estructuras de datos como argumentos de nuestras funciones, lo que será particularmente útil cuando queramos aplicarlas sobre **NumPy Arrays** o incluso sobre **DataFrames**. Para el caso del cálculo de notas, por ejemplo, puede parecernos útil definir una función que calcule el promedio de una lista de valores. 

def promedio_lista(lista):
    suma=0
    for i in lista:
        suma = suma + i
    promedio = round(suma/len(lista),1)
    print(promedio)

promedio_lista([5,4.7,6.5])

"""" for i in lista: significa "para cada elemento i en la lista, ejecutar el siguiente bloque de código".
suma = suma + i: suma el valor actual de i a la variable suma, acumulando los valores. 
suma / len(lista)

suma contiene la suma de todos los elementos de la lista.
len(lista) obtiene la cantidad de elementos en la lista.
Se divide suma entre la cantidad de elementos para calcular el promedio.
round(..., 1)

La función round(valor, 1) redondea el resultado a un decimal."""