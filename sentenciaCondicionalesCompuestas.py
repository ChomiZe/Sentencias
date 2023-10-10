print("Sistema para calcular el prodio de un alumno.")

nombre = input("Ingrese su nombre para comenzar: ")

matematicas = float(input(nombre + " Ingrese su calificación de matemáticas: "))
quimica = float(input(nombre + " Ingrese su calificación de química: "))
fisica = float(input(nombre + " Ingrese su calificación de Física: "))

promedio = (matematicas + quimica + fisica) / 3

if promedio >= 6:
    print('Felicidades '+nombre+ ' "aprobaste" con un promedio de: ', promedio)
    #round cantidad de decimales a mostrar
    print('Felicidades '+nombre+ ' "aprobaste" con un promedio de: ', round (promedio,2))

else:
    print("Lo sentimos "+ nombre + " no has aprobado tu promedio fue de: ", promedio)
     #round cantidad de decimales a mostrar
    print("Lo sentimos "+ nombre + " no has aprobado tu promedio fue de: ", round (promedio,1))

print("Fin")
