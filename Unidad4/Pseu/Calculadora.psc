Algoritmo Calculadora
	Escribir "Calculadora"
	Escribir "Que desea hacer?"
	Escribir "1=Sumar	 2=Restar 		3=Multiplicar  		4=Dividir"
	Leer A 
	Escribir "Ingresa el primer valor; "
	Leer N1
	Escribir "Ingresa el segundo valor; "
	Leer N2
	B1 = N1+N2
	B2 = N1*N2
	B3 = N1-N2
	B4 = N1/N2
	Segun x Hacer
		1:
			Imprimir  "Resultado; ", B1
		3:
			Imprimir "Resultado; ", B3
		2:
			Imprimir "Resultado; ", B2
		4:
			Imprimir "Resultado; ", B4
		De Otro Modo:
			Imprimir "Error"
	Fin Segun	
FinAlgoritmo
