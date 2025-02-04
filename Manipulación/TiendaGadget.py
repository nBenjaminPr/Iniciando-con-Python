import pandas as pd
import numpy as np

#Creamos el Data Frame de usuaiors

usuarios = {
    'id_usuario': [1, 2, 3, 4, 5],
    'nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luisa'],
    'edad': [25, 30, 45, 22, 28]
}

df_usuarios = pd.DataFrame(usuarios)

#Creamos el DataFrame de pedidos

pedidos = {
    'id_pedido': [1, 2, 3, 4, 5, 6, 7, 8],
    'id_usuario': [1, 2, 3, 3, 4, 4, 4, 5],
    'fecha': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02', '2022-01-02', '2022-01-03', '2022-01-03', '2022-01-04'],
    'producto': ['A', 'B', 'A', 'B', 'A', 'A', 'B', 'A'],
    'cantidad': [10, 5, 12, 8, 5, 6, 6, 15],
    'precio': [100, 50, 120, 80, 150, 150, 100, 90]
}

df_pedidos = pd.DataFrame(pedidos)


#Podemos hacer el cruce con la columna común que tienen ambos DataFrames llamada 'id_usuario', para unir las tablas

df_pedidos = df_pedidos.set_index("id_usuario")

df_marger = df_pedidos.merge(df_usuarios, on="id_usuario",how="outer")

#Creacion de columnas calculadas
#Creamos una columna de Monto de ventas = a la cantidad multiplicado por el precio
df_marger["monto_venta"] = df_marger["cantidad"] * df_marger["precio"]

df_marger.to_csv("resultado.txt", sep="\t", index=False)

print (df_marger)