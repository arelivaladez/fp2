Nombre = input("Ingresar el nombre; ") 
Nombre2 = input("Ingresar el segundo nombre; ") 
z =  len(Nombre)
x =  len(Nombre2)

if z > x: 
	print ("Cantidad de caracteres: ", z)
	print (Nombre)
else:
	print ("Cantidad de caracteres: ", x)
	print (Nombre2)