print("Sistema para calcular el prodio de un alumno.")

nombre = input("Ingrese su nombre para comenzar: ")

matematicas = int(input(nombre + " Ingrese su calificación de matemáticas: "))
quimica = int(input(nombre + " Ingrese su calificación de química: "))
fisica = int(input(nombre + " Ingrese su calificación de Física: "))

promedio = (matematicas + quimica + fisica) / 3
promedio = int(promedio)#convierte el promedio decimal en entero

if promedio >= 6:
    print('Felicidades '+nombre+ ' "aprobaste" con un promedio de: ', promedio)

print("Fin")
