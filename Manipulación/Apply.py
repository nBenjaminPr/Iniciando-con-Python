import pandas as pd

#uso del applymao()

data = {'texto': ['Hoy es un gran día para empezar a aprender algo nuevo! #motivación','Estoy muy emocionado por el partido de esta noche! #vamosequipo','Qué triste noticia la pérdida de un gran artista como Chadwick Boseman #RIPChadwickBoseman','¡Qué maravilloso día en el parque con la familia! #familia #naturaleza #airelibre','No puedo creer lo que acabo de ver en las noticias. #indignación #justiciaparaMauricio','¡Feliz cumpleaños a mi mejor amiga! #amistad #celebración #cumpleaños'],'texto2': ['Hoy hace un día increíble en la playa! #playa #verano', 'Acabo de ver la última película de mi actor favorito. ¡Qué actuación increíble! #cine #actuación','Estoy emocionado por mi próximo viaje a Europa. ¡No puedo esperar para explorar nuevos lugares! #viaje #exploración','Acabo de comenzar a leer un nuevo libro y ya estoy enganchado. #lectura #libros','¡Feliz día de la independencia a todos! #díadelaindependencia #patriotismo #fiesta','Aprendiendo a programar hoy. ¡Es difícil pero emocionante! #programación #desarrollo']}

df5 = pd.DataFrame(data)

df5 = df5.applymap(lambda x: [i for i in x.split() if "#" in i])

print (df5)