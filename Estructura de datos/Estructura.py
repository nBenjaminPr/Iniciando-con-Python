frutas_favoriras = ["Pera", "Manzana","Uva", "Fresa"]

#Preguntar al usuario por una nueva fruta
nueva_fruta = input("Agregar nueva fruta: ")
frutas_favoriras.append(nueva_fruta)

#Preguntar al usuario por eliminar una fruta
frutas_eliminada = input ("Elimine una fruta de la lista: ")
frutas_favoriras.remove(frutas_eliminada)

#Para ordear alfabeticamente
frutas_favoriras.sort()

#Mostrar lista completa
print("Lista de frutas favoritas: ")
for fruta in frutas_favoriras:
    print("-", fruta)
    