import random

a = random.randint(1,20)

intentos=0

while intentos < 5:
    respuesta = int(input (" ingrese un numero: "))
    intentos += 1
    if respuesta < a:
        print("es mayor")
    if respuesta > a:
        print("es menor")
    if respuesta == a:
        break

    if respuesta == a:
        print(f"!has adivinado")
    else:
        print(f"intentos {5 - intentos}")
        