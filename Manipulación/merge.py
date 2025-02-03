import pandas as pd
import numpy as np
#Lista de Rubros
rubros = ["Calzado", "Remera", "Pantalones","Gorras"]
n_rubros = len(rubros)

# Creamos un DataFrame de los rubros de venta

df_rubros = pd.DataFrame({"id_rubros": range(0,n_rubros), "des_rubro": rubros})

print (df_rubros)