#Este método se utiliza para crear variables binarias o "dummy variables" a partir de variables categóricas. Las variables binarias son columnas de valores 0 o 1 que indican la presencia o ausencia de una categoría en particular.

#Por ejemplo, si tenemos una columna que indica la nacionalidad de un grupo de personas en el aeropuerto, podemos usar **pd.get_dummies()** para crear dos nuevas columnas, una para pasajeros nacionales y otra para extranjeros, y marcar con 1 la columna correspondiente a cada caso, lo que facilita el análisis de los datos categóricos. Observa el ejemplo:

import pandas as pd

data = {
    'Pasajero': ['Juan', 'María', 'Pedro', 'Laura', 'Francisca'],
    'Nacionalidad': ['N', 'N', 'E', 'N', 'E']
}

df = pd.DataFrame(data)

df = pd.get_dummies(df, columns = ['Nacionalidad'],drop_first = True)

print (df)