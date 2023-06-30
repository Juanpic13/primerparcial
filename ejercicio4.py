# ejercicio 4: Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales,
# indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6).

"se le pide que se ingresen las notas"
notas = 0 
prom = 0
while notas<3:
 calificacion = float(input("ingrese la calificacion obtenida: "))
 notas = notas + 1 
 prom = prom + calificacion
promedio = prom/notas
if promedio <=5 :
 print("el alumno debe recursar la materia ")    
else :
 print("el alumno aprobó la materia ")