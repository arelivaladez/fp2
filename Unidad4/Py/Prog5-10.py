#ClaseyAtributo
Clas = input("Ingresar nombre de la clase: ")
Atri = input("Ingresar 5 atriburos")

class Matematicas:
	"""docstring for ClassName"""
	def __init__(self, cla1, cla2, cla3, cla4, cla5):
		self.cla1 = cla1
		self.cla2 = cla2
		self.cla3 = cla3
		self.cla4 = cla4
		self.cla5 = cla5
A = input("Ingresar 1er atributo: ")
R = input("Ingresar 2do atributo: ")
E = input("Ingresar 3er atributo: ") 
L = input("Ingresar 4to atributo: ")
I = input("Ingresar 5to atributo: ")
Cls1 = Matematicas(A, R, E, L, I)

Array = [Cls1.cla1, Cls1.cla2, Cls1.cla3, Cls1.cla4, Cls1.cla5]
print("La clase es: ", Clas)
print("Los atributos son: ", Array)
		
