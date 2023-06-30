# ejercicio 1 : Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, basado en el año de nacimiento.
"se solicita al usuario ingresar su nacimiento y fecha actual "
nacimiento = int(input("Ingrese su año de nacimiento: "))
fecha_actual = int(input("Ingrese el año actual: "))
"Cálculo para saber la edad a cumplir en el año actual"
edad = fecha_actual - nacimiento
print ("este año deberias cumplir o cumpliste ", edad, " años.")  