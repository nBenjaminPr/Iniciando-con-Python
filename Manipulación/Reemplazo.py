import pandas as pd
import numpy as np

data = {'producto':['camiseta negro S','camiseta rojo S','camiseta negro S','camiseta azul L','camiseta azul M','pantalón azul M','zapatos negro L','zapatos rojo L','zapatos azul L'],
        'precio': np.random.randint(1000, 5000, 9)}

df = pd.DataFrame(data)

#Reemplazo de datos
df = df.replace('camiseta negro S', 'camiseta - agotada')

#Reemplazo usando codigos
replace_dict = {'camiseta negro S': 'camiseta - agotada', 'pantalón azul M': 'pantalón - agotado'}
df_replaced = df.replace(replace_dict)

print(df_replaced)

