#Area de figuras

print("¿De que figura quieres sacar el area?")
print("1= circulo", "2= cuadrado", "3= rectangulo", "4= triangulo")
area = int(input("Ingresar numero: "))

if area == 1:
	C = int(input("Dar el radio: "))
	D =C**2
	A = 3.1416*D
	print ("El area del circulo es: ", A)
elif area ==2:
	Dro = int(input("Dar el lado del cuadrado: "))
	print("El area del cuadrado es: ", Dro**2)
elif area == 3:
	Rec = int(input("Dar la altura del rectangulo: "))
	Tan = int(input("Dar la base del rectangulo: "))
	print ("El area del rectangulo es: ", Rec*Tan)
elif area == 4:
	Tri = int(input("Ingresar la altura del triangulo: "))
	Ba = int(input("Ingresar la base del triangulo: "))
	print("El area es: ", (Tri*Ba)/2)
else:
	print("Error")
print("FIN")