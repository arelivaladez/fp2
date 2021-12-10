Algoritmo Areadefiguras
	Escribir " 1= circulo, 2= cuadrado, 3= rectangulo, 4=triangulo"
	Leer area
	Segun area Hacer
		1:
			escribir "Dame el radio; "
			leer Radio
			Escribir "El area es; " 3.1416*(Radio^2)
		2:
			Escribir "Dar el area"
			Leer Cua
			Escribir "El area es: " Cua^2
			
		3:
			Escribir "Dar Altura del Rectangulo"
			Leer are2
			Escribir "Dar la base del Rectangulo"
			Leer P
			Escribir "El area es: ", P*are2
		4:
			Escribir "Ingresar la Altura del triangulo"
			Leer tri
			Escribir "Dar la base del triangulo"
			Leer Ba
			Escribir "El area es: ", (Ba*tri)/2
	Fin Segun
	
FinAlgoritmo
