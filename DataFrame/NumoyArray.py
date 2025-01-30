import pandas as pd
import numpy as np

datos = {"nombre": ["Juan","Maria","Pedro"]
        ,"edad": [25,18,45],
        "Ciudad": ["Arg","Brz","Eeuu"]}

df3 = pd.DataFrame(datos)

print(df3)

arr = np.array ([[1,2], [3,4]])
df5 = pd.DataFrame (arr, columns= ["A", "B"])
print(df5)