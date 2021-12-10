#Calculadora

print("1=Sumar 		2=Restar 	3=Multiplicar 	4=Dividir")
	A = int(input("¿Que deseas hacer?"))
	if A == 1:
		N1 = int(input("Ingresar el primer valor; "))
		N2 = int(input("Ingresar el segundo valor; "))
		print("El resultado es; ", N1+N2)
	elif A == 3:
		N1 = int(input("Ingresar el primer valor; "))
		N2 = int(input("Ingresar el segundo valor; "))
		print("El resultado es; ", N1*N2)
	elif A == 2:
		N1 = int(input("Ingresar el primer valor; "))
		N2 = int(input("Ingresar el segundo valor; "))
		print("El resultado es; ", N1-N2)
	elif A == 4:
		N1 = int(input("Ingresar el primer valor; "))
		N2 = int(input("Ingresar el segundo valor; "))
		print("El resultado es; ", N1/N2)
	elif A == 5:
		print("Error")

print ("FIN")