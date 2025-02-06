import pandas as pd

data = {
    'Empleados': ['Juan', 'María', 'Pedro', 'Luis', 'Francisca'],
    'Fecha_Incorporacion': ['2022-10-01', '2022-03-01', '2022-05-01', '2021-12-01', '2023-03-01']
}

df=pd.DataFrame(data)

print (df)