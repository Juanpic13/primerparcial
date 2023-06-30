#ejercicio 10: Escribe un programa que calcule el promedio general de una clase.


"pedimos la cantidad de alumnos "
alumnos = int(input("¿Cuántos alumnos hay en la clase?: ")) 
alumno = 1
notas= 0

while alumno <= alumnos: 
    nota =float(input("Ingresar nota: "))
    notas = notas + nota 
    alumno = alumno + 1 
    

promedio_clase = notas / alumnos #se calcula el promedio 
print( " Promedio general: ", promedio_clase) # se muestra el promedio 

