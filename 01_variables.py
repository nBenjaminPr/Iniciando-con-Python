# Variables

my_variable = "My String Variable" #18 caracteres
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


my_bool_variable = False
print(my_bool_variable)

#Concatenacion de variables en un print

print (type(print(my_variable, my_int_to_str_variable,my_bool_variable)))
print("Este es el valor de :", my_variable)


# Funciones del Sistema

print(len (my_variable)) #Cuenta los caracteres

# Varaible en una sola linea, es una mala practica

name, surname, alias, age = "Nico", "Cachi", "piter", 25
print("Me llamo: ",name,surname,"Mi edad es:", age,"y mi alais es:", alias)

# INPUT

#name= input("Cual es tu nombre ")
#age = input("Cuantos años tiene ")

#print(name)
#print(age)

# Cambiamos su tipo ¡Cuidado!

#name = 35
#age = "Pedro"
#print(name)
#print(age)

# Forzamos un tipo

address: str = "Mi direcciòn"
address = 32
address = True
address = 0.5
print(address)