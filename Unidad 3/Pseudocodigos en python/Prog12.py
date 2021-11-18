#Nombre y Edad Mayor 
Nombre1 = input("Ingresar Nombre")
ED1 = int(input("Ingrasar Edad"))
Nombre2 = input("Ingresar Nombre")
ED2 = int(input("Ingresar Edad"))

if ED1 > ED2:
	print(Nombre1, ED1)
elif ED1 < ED2: 
	print(Nombre2, ED2)
else:
	print("Datos no validos")

print("FIN")