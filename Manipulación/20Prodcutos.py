import pandas as pd
import numpy as np

#Generamos 20 ventas

n_ventas = 20

df_ventas = pd.DataFrame(

    {
        "Id_venta": range(0, n_ventas),
        "Rubro" : np.random.randint(0,n_ventas,n_ventas),
        "Precio": np.random.randint( 2400,10000,n_ventas),
        "cantidad": np.random.randint(1,7,n_ventas)
    }
)

print(df_ventas)