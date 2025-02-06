import pandas as pd

# Crear un DataFrame de ejemplo
df = pd.DataFrame({'fecha': ['2022-05-02', '2022-05-03', '2022-05-04']})

# Convertir a formato de fecha y hora de Pandas
df['fecha'] = pd.to_datetime(df['fecha']) #format='%d-%m-%Y'

# Extraer el mes de la fecha
df['mes'] = df['fecha'].dt.month

# Extraer el nombre del mes de la fecha
df['nombre_mes'] = df['fecha'].dt.month_name()

# Verificar el resultado
print (df)