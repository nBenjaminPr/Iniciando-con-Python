#**D**on´t **R**epeat **Y**ourself (No lo repitas tú mismo) es un principio básico en programación, que apunta a que busquemos no "copiar y pegar" por nosotros mismos los códigos, y confiar a una función todas las tareas repetitivas que sea posible. En ocasiones, hacer esto puede parecer más complejo ya que nos hace definir más funciones, pero a la larga, si tenemos que utilizar muchas veces un cálculo determinado puede terminar resultando más útil rear algunas herramientas y luego utilizarlas, lo que nos permitirá obtener códigos más limpios.

#En nuestro caso, por ejemplo, definir la función **promedio_lista** nos permite utilizarla luego **para cualquier lista de valores** sin necesidad de modificar el parámetro correspondiente a la cantidad de notas, por ejemplo.

### <font color='green'>Buenas prácticas</font>

#### Comentarios y Docstrings

#Cuando escribimos funciones, no solo queremos que cumplan con su propósito y sean eficientes sino que también que sean fáciles de entender y utilizar. Para ello, siempre se recomienda añador los comentarios que puedan ser necesarios para aclarar cada paso de nuestro programa o de las funciones que creemos; en particular para las funciones utilizaremos los **docstrings**.

#Un **docstring** es una cadena de texto que se ubica como el primer elemento dentro de la definición de una función, entre tres pares de comillas dobles para crear un bloque de comentario. Proporciona una descripción concisa de lo que hace la función, los parámetros que espera y el valor que retorna, si lo tiene.

#Los docstrings son útiles para documentar y comunicar claramente la funcionalidad de nuestras funciones, ayudando a otros programadores (incluido nosotros mismos en el futuro) a utilizar y comprender correctamente el código.



def area_triangulo (base,altura):

    area = (base * altura) / 2

    return area