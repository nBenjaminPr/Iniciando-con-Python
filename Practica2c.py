tienda = int(input ("Ingrese valor del producto: "))

cantindad = int(input ("Ingrese cantidad de productos: "))

total = tienda * cantindad

if total >= 1500:
    print (total,"El envio es express")
elif total >= 1000 and total < 1500:
    print (total, "El envio es gratis")
elif total >= 500 and total < 1000:
    print (total, "El envio es tiene un costo de 10 euros")
elif total < 500:
    print (total, "Su pedido no se puede procesar")

    