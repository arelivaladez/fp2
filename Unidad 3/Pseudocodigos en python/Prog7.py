#Imprime el numero mayor
Numero1 = int(input("Ingresar 1er numero"))
Numero2 = int(input("Ingresar 2do numero"))

if Numero1 < Numero2:
	print(Numero2)
elif Numero1 > Numero2:
	print(Numero1)
else: 
	print("Dados incorrectos")

print("FIN")