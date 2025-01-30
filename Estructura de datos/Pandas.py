# Una lista de diccionarios.

import pandas as pd

lista_de_diccionarios = [

    {'nombre': 'Ana', 'profesion': 'guitarra', 'edad': '34'},
    {'nombre': 'Luis', 'profesion': 'fotógrafo', 'edad': '27'},
    {'nombre': 'María', 'profesion': 'profesora', 'edad': '42'},
    {'nombre': 'Pedro', 'profesion': 'chef', 'edad': '39'},
    {'nombre': 'Isabel', 'profesion': 'arquitecta', 'edad': '29'},
    {'nombre': 'Sergio', 'profesion': 'músico', 'edad': '25'},
    {'nombre': 'Carla', 'profesion': 'ingeniera', 'edad': '31'},
    {'nombre': 'David', 'profesion': 'estudiante', 'edad': '20'},
    {'nombre': 'Lucía', 'profesion': 'abogada', 'edad': '36'},
    {'nombre': 'Jorge', 'profesion': 'actor', 'edad': '28'}

]

df = pd.DataFrame(lista_de_diccionarios)
df

# Una lista de listas. (listas anidadas):

lista_anidada = [

    ['Ana', 'guitarra', '34'],
    ['Luis', 'fotógrafo', '27'],
    ['María', 'profesora', '42'],
    ['Pedro', 'chef', '39'],
    ['Isabel', 'arquitecta', '29'],
    ['Sergio', 'músico', '25'],
    ['Carla', 'ingeniera', '31'],
    ['David', 'estudiante', '20'],
    ['Lucía', 'abogada', '36'],
    ['Jorge', 'actor', '28']
]


df = pd.DataFrame(lista_anidada, columns = ['nombre', 'profesion', 'edad'])
df