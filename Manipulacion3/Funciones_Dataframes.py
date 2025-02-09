#Observa que al principio de nuestro bloque hemos definido la variable **t = 18**, y luego hemos utilizado este valor dentro de una función. A la variable **t** se le ha asignado un valor **global**, es decir, fuera del entorno de una función, por lo que es posible acceder a ella desde cualquier parte del programa.

import pandas as pd

df = pd.DataFrame({'A': [1, 2], 'B': [10, 20]})


def square(x):
    return x * x


df1 = df.apply(square)

print(df)
print(df1)