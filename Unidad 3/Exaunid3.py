#Desarrollar un programa que guarde a todos los integrantes del grupo como objetos
#con los siguientes atributos: Edad, Calificacion de los diferentes materias, promedio, 
#calificacion de la prepa y lugares de residencia. 
#Imprimir o mostrar los siguientes reportes:
#5 alumnos con mayor edad (dias incluidos)
#Promedio de toda la preparatoria 
#Alumnos que viven mas cerca y mas lejos
#Materia con mejor rendimiento.

#crear clase
class Alumno():
 	def __init__ (self,E,N,C,F,I,T,ET,IN,MD,CP,LR,DT):
 		self.N= N
 		self.E = E
 		self.C = C 
 		self.F = F
 		self.I = I 
 		self.T = T
 		self.ET = ET
 		self.IN = IN 
 		self.MD = MD
 		self.CP = CP 
 		self.LR = LR
 		self.DT=DT

#crear objetos
reyna = Alumno(18,"Reyna", 6, 7, 5, 10, 8, 5, 9, 9, "Emiliano Zapata", 13)
mirozlava = Alumno(18,"Mirozalva",9, 8, 10, 7, 9, 6, 7, 8, "Cosio", 27)
mely = Alumno (18,"Melany", 7, 8, 7, 5, 9, 10, 7, 9, "pabellon", 5)
diego = Alumno(19,"Diego", 8, 9, 9, 10, 8, 8, 10, 10, "rincón", 13) 
britzy = Alumno(18,"Britzy", 10, 9, 10, 10, 8, 8, 10, 10, "rincón", 13) 
fernando = Alumno(17, "Fernando", 8, 8, 7, 9, 10, 8, 10, 9, "pabellon", 5)
alejandra = Alumno(18,"Alejandra", 10, 10, 10, 10, 10, 10, 10, 8, "jesus maria", 27)
alejandro= Alumno(19, "Alejandro", 10, 9, 8, 9, 8, 9, 8, 9, "Ejido Fresnillo", 17)
donaldo= Alumno(18, "Donaldo", 8, 9, 10, 9, 8, 6, 8, 8, "San Jose de Gracia", 18)
austin= Alumno(18, "Austin", 10, 9, 8, 9, 10, 9, 8, 8, "pabellon", 5)
paola=Alumno(18,"Paola", 10, 9, 8, 9, 10, 9, 8, 8, "carboneras", 8)
isaac=Alumno(19, "Isaac", 10, 9, 10, 9, 10, 10, 10, 9, "rincon", 13)
areli=Alumno(19, "Areli", 10, 9, 10, 9, 10, 9, 10, 8, "rincon", 13)
alain=Alumno(18, "Alain", 10, 9, 10, 9, 10, 9, 10, 8, "asientos", 11)
alexis=Alumno(19, "Alexis", 10, 9, 10, 8, 7, 8, 7, 8, "rincon", 13)

print ("los alumnos con mayor edad son ", diego.N,",",alejandro.N,",",isaac.N,",",areli.N,"y",alexis.N )

print ("los alumnos y sus calificaciones se presentaran a continuación\n", reyna.N,"con promedio de",reyna.CP,",\n",mirozlava.N,"con promedio de",mirozlava.CP)
print(mely.N,"con promedio de",mely.CP,",\n",diego.N,"con promedio de",diego.CP,",\n",britzy.N,"con promedio de",britzy.CP)
print(fernando.N,"con promedio de",fernando.CP,",\n",alejandra.N,"con promedio de",alejandra.CP,",\n",alejandro.N,"con promedio de",alejandro.CP)
print(donaldo.N,"con promedio de",donaldo.CP,",\n",austin.N,"con promedio de",austin.CP,",\n",paola.N,"con promedio de",paola.CP)
print(isaac.N,"con promedio de",isaac.CP,",\n",areli.N,"con promedio de",areli.CP,",\n",alain.N,"con promedio de",alain.CP,",\n",alexis.N,"con promedio de",alexis.N)

print("Los alumnos que viven mas lejos del tec son:\n",mirozlava.N,"es de ",mirozlava.LR, "con una distancia de", mirozlava.DT, "y\n", alejandra.N, "es de", alejandra.LR, "con una distancia de",alejandra.DT )
print("Los alumnos que viven mas cerca del tec son:\n",mely.N,"es de ",mely.LR, "con una distancia de", mely.DT, "y\n", donaldo.N, "es de", donaldo.LR, "con una distancia de",donaldo.DT )


print ("los alumnos y sus mejoras se presentaran a continuación\n", reyna.N,"con la meteria de fundamentos de la programacion",",\n",mirozlava.N,"con la meteria de fundamentos de la investigación")
print(mely.N,"con la materia de fundamentos de la investigacion",",\n",diego.N,"con la materia de fundamentos de mates discretas",",\n",britzy.N,"con la materia de calculo diferencial")
print(fernando.N,"con la materia de matematicas discretas",",\n",alejandra.N,"con la materia de introduccion a las tics",",\n",alejandro.N,"con la materia de calculo diferencial")
print(donaldo.N,"con la materia de calculo diferencial",",\n",austin.N,"con la materia de ingles ",",\n",paola.N,"con la materia de calculo diferencial ")
print(isaac.N,"con la materia de calculo diferencial",",\n",areli.N,"con la materia de fundamentos de la investigacion",",\n",alain.N,"con la materia de ingles",",\n",alexis.N,"con la materia de calculo diferencial ")
