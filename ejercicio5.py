# ejercicio 5: Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas 
# y muestre por pantalla el resultado, considerando lo siguiente:
#  a. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.
#  b. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.
#  c. Si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100.
"se solicita ingresar las horas trabajadas en el mes"
horas_trabajadas = float(input("Ingrese la candidad de horas trabajadas en el mes: "))
"se calcula el sueldo dependiendo las horas trabajadas"
sueldo1 = horas_trabajadas * 1500
sueldo2 = horas_trabajadas * 1300
sueldo3 = horas_trabajadas * 1100
"se muestra el sueldo"
if horas_trabajadas > 120:
    print("Su sueldo es: $", sueldo1) 
elif horas_trabajadas <= 120 and horas_trabajadas >= 80: 
    print("Su sueldo es: $", sueldo2) 
else:
    print("Su sueldo es: $", sueldo3) 

