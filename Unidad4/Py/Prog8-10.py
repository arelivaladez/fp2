#Nombre aleatorio

N = input("Ingresar el nombre: ")
Nob = len(N)

import string, random
C = string.ascii_letters

if __name__ == '__main__':
	rstr = random.choice(string.ascii_letters)

	print("El nombre es: ", N)
	print("El nombre aleatorio es: ", (rstr*(len(N))))

print("FIN")