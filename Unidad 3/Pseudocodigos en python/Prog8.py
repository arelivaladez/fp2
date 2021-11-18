#Programa que pide 3 numeros e imprime el mayor
Nu1 = int(input("Ingresar 1er valor: "))
Nu2 = int(input("Ingresar 2da valor: "))
N3 = int(input("Ingresar 3er valor: "))

if Nu1 > Nu2 and N3:
	print(Nu1)
elif Nu2 > Nu1	and Nu3:
	print(Nu2)
elif N3 > Nu2 and Nu1:
	print (Nu3)
else:
 	print("Datos Incorrectos")

print ("Final") 