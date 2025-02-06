import pandas as pd

data = {
    'Empleados': ['Juan', 'María', 'Pedro', 'Luis', 'Francisca'],
    'Fecha_Incorporacion': ['2022-10-01', '2022-03-01', '2022-05-01', '2021-12-01', '2023-03-01']
}

df=pd.DataFrame(data)

#convierte una columna de tipo cadena de texto en formato de fecha, a un objeto de fecha y hora de Pandas
df['Fecha_Incorporacion'] = pd.to_datetime(df['Fecha_Incorporacion'])

#Algunos de los parámetros más importantes que acepta pd.to_datetime son:
#- **arg:** Es el argumento que se va a convertir a fecha y hora. Puede ser una cadena, una lista de cadenas o una serie de Pandas.
#- **format:** Es el formato de la cadena de fecha y hora. Si no se especifica, Pandas intentará adivinar el formato.
#- **dayfirst:** Un booleano que indica si el primer elemento de la cadena de fecha y hora es el día. Si se establece en True, Pandas interpreta la fecha y hora con el formato día/mes/año.
#- **yearfirst:** Un booleano que indica si el primer elemento de la cadena de fecha y hora es el año. Si se establece en True, Pandas interpreta la fecha y hora con el formato año/mes/día.

df = df['Fecha_Incorporacion'].dt.month

#Al utilizar .dt en una columna de un DataFrame en pandas, se puede acceder a una variedad de métodos y propiedades relacionados con fechas y horas. A continuación, se presentan algunos de los métodos y propiedades comunes disponibles al utilizar .dt:

#- year: Devuelve el año de cada valor de fecha/hora.
#- month: Devuelve el mes de cada valor de fecha/hora.
#- day: Devuelve el día del mes de cada valor de fecha/hora.
#- hour: Devuelve la hora de cada valor de fecha/hora.
#- minute: Devuelve los minutos de cada valor de fecha/hora.
#- second: Devuelve los segundos de cada valor de fecha/hora.
#- microsecond: Devuelve los microsegundos de cada valor de fecha/hora.
#- nanosecond: Devuelve los nanosegundos de cada valor de fecha/hora.
#- weekday: Devuelve el día de la semana (como un número, donde 0 es lunes y 6 es domingo) de cada valor de fecha/hora.
#- month_name: Devuelve el nombre del mes de cada valor de fecha/hora.
#- day_name: Devuelve el nombre del día de la semana de cada valor de fecha/hora.
#- is_leap_year: Devuelve un booleano que indica si cada valor de fecha/hora corresponde a un año bisiesto.

#Puedes utilizar los métodos de los objetos de fecha y hora de Pandas para extraer información específica de las fechas. Por ejemplo, puedes utilizar el método dt.month para extraer el mes de una fecha y dt.month_name() para obtener el nombre del mes en inglés.

print (df)
