Algoritmo Nombre_Letras_Aleatoria
	Definir N Como Entero
	Definir Nob, A Como Caracter
	Escribir "Dar el nombre"
	Leer Nob
	N = Longitud(Nob)
	A = " "
	Mientras N > 1 Hacer
		A = A +Subcadena(Nob, N, N)
		N = azar(50)
	Fin Mientras
	Escribir "El nombre es; " Nob " de forma aleatoria; " A
FinAlgoritmo
