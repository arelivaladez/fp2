numero = 8
running = True

while running:
    Nombre = input("Ingresar el nombre del alumno")
    Cal = int(input('Ingresar la calificacion obtenida'))

    if Cal > numero:
        print(Nombre)
        print("Aprovado")
    elif Cal < numero:
        print(Nombre)
        print("Reprobo")
    else:
        print(Nombre, "Reprobo")
else:
    print("Bucle Finalizado")
   

print('Fin')