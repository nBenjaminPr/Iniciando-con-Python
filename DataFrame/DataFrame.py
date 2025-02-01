import pandas as pd
import numpy as np

#Agregamos el diccionario con sus listas (columnas)
df_dias = pd.DataFrame({"dias_laborables": ["Lunes","Martes","Miercoles", "Jueves","Viernes"]})

# Se agrega la comlumna y despues la lista
df_dias["dias_no_laborables"] = ["Sabado", "Domingo","","",""]

df_dias["Feriados"] = [14,9,25,1,2 ]

print (df_dias)

df_nombres = pd.DataFrame ({"Nombres": ["Lucas", "Juan", "Maria", "Pedro"]})

df_nombres["nombres_perfil1"] = ["Sr.","Sr.","Srta.","Sr"] + df_nombres["Nombres"]

df_nombres["edad"] = np.random.randint(18, 100, 4)

print (df_nombres)


