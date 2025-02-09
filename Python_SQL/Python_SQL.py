import pandas as pd

#Para mostrar el funcionamiento de los comandos que nos interesan utilizaremos una base de datos de prueba llamada **northwind**, que es propiedad de Microsoft pero que permite su uso para el aprendizaje de SQL. Para crear la base de datos necesitarás primero tenerla descargada en tu equipo, abrir una terminal y ejecutar los siguientes comandos:

#Para crear la base de datos:
#- psql -h localhost -p 5432 -U postgres -c "CREATE DATABASE northwind"

#Para cargar los datos del archivo:
#- psql -h localhost -p 5432 -U postgres -d northwind -f northwinddb.sql

#Crearemos ahora un **string de conexión** para realizar de manera más limpia nuestro trabajo. Para ello escribimos



#En este caso, "password" es la contraseña que hemos fijado para el usuario **postgre** (podemos usar otro usuario y otra contraseña, siempre que el usuario tenga acceso a la base de datos.

#El paso siguiente es crear un **objeto de conexión** utilizando el método create_engine de la librería sqlalchemy.  Cada vez que hagamos una petición a la base de datos con Pandas utilizaremos este objeto de conexión que dentro de la documentación de la librería sqlalchemy se conoce como **engine**.

