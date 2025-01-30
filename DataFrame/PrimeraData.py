import pandas as pd

data = {
    "Nombre": ["Ana", "Juan", "Luis"],
    "Edad": [25, 30, 22],
    "Ciudad": ["Madrid", "Buenos Aires", "México"]
}

df = pd.DataFrame(data)

df = df.set_index ("Nombre")

# Mostrar el DataFrame
print(df)