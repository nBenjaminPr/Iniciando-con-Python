import pandas as pd
import numpy as np
#Lista de Rubros
rubros = ["Calzado", "Remera", "Pantalones","Gorras"]
n_rubros = len(rubros)

# Creamos un DataFrame de los rubros de venta

df_rubros = pd.DataFrame({"id_rubro": range(0,n_rubros), "des_rubro": rubros})


# Generaremos 100 ventas.

n_ventas = 20

df_ventas = pd.DataFrame(

    {
        "Id_venta": range(0, n_ventas),
        "rubro" : np.random.randint(0,n_ventas,n_ventas),
        "Precio": np.random.randint( 2400,10000,n_ventas),
        "cantidad": np.random.randint(1,7,n_ventas)
    }
)

#vamos a cruzar ambas tablas, considerando que en ambas se considera el rubro #(con identificador) **aunque reciben nombres diferentes en cada tabla**. Por lo #mismo, deberemos utilizar los parámetros

#- **left_on:** columna(s) a cruzar por la izquierda.
#- **right_on:** columnas(s) a cruzar por la derecha.

#Además, habrá varias ventas por la izquierda a las que les corresponderá **un** #elemento de la tabla por la derecha. Por lo mismo, utilizaremos la validación #**many_to_one**

df_merged = df_ventas.merge(df_rubros, left_on="rubro", right_on="id_rubro",validate="many_to_one")

print (df_merged)
