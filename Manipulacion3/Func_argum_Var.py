def potencia (base,exponente = 1):
    return (base ** exponente)

print (potencia(3)) # Sin especificar exponente, toma el valor por defecto (1)
print (potencia(3,4)) # Calcula 3(base)^4 (exponente)

"""Funciones con argumente"""
#Otro aspecto interesante de Python es que nos permite utilizar funciones como argumento de una función y con ello, por ejemplo, evaluar listas de funciones. Para utilizarlas, será necesario ingresar su nombre **sin paréntesis**, como se muestra:

def funciona(a):
    return(a+4)

def funcionb(b):
    return(6*b)

def funcionc(c):
    return(2*c-5)

for y in [funciona,funcionb,funcionc]:
    print(y(5))


#Variables locales y globales
#Observa que al principio de nuestro bloque hemos definido la variable **t = 18**, y luego hemos utilizado este valor dentro de una función. A la variable **t** se le ha asignado un valor **global**, es decir, fuera del entorno de una función, por lo que es posible acceder a ella desde cualquier parte del programa.

t = 18 #t= Variable Global

def sumat(a):
    g = a + t
    r = 2*g   #G y R son variables locales
    return(r)

print (sumat(8))

#Observa que al principio de nuestro bloque hemos definido la variable **t = 18**, y luego hemos utilizado este valor dentro de una función. A la variable **t** se le ha asignado un valor **global**, es decir, fuera del entorno de una función, por lo que es posible acceder a ella desde cualquier parte del programa.

def funcion_prueba(s):
    t = s + 5 #Valores locales
    print(t)

funcion_prueba(3)

print(t) #Valor global

