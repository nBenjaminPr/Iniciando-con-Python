#Si no indicamos con .str que queremos acceder a métodos de la clase string, entonces arrojará un error indicando que una columna de tipo pd.Serie no tiene un método llamado .lower(). De la misma forma podemos acceder a cualquier método propio de la clase string, entre ellos:

"""- str.upper()
- str.lower()
- str.isupper()
- str.islower()
- str.isnumeric()
- str.replace()
- str.split()
- str.contains()
- str.find()
"""

import pandas as pd

data = {
    'Pasajero': ['Juan', 'María', 'Pedro', 'Laura', 'Francisca'],
    'Nacionalidad': ['N', 'N', 'E', 'N', 'E']
}

df = pd.DataFrame(data)

df = df['Pasajero'].str.find()

print (df)