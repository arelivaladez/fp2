Nombre = input('Ingresar Nombre: ')
Promedio = 7
Cal = int(input('Ingresar la calificacion '))

if Cal > Promedio:
    print(Nombre)
    print("Aprobo")
    
elif Cal <  Promedio:
    print(Nombre)
    print('Reprobado')

else:
    print('Error, calificacion invalida')
    

print('Fin')