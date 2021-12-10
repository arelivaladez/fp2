#Sorteo
K = int(input("Ingresa la cantidad del 1 al 10: "))
import random
C = random.randint(1,10)

if K == C:
	print(K, "Felicidades Ganaste")
else: 
	print(K, "Perdiste")

print("FIN")