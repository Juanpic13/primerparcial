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

"se calculan las bonificaciones"
bonificacion1 = sueldo1 * 0.18 
bonificacion2 = sueldo2 * 0.15
bonificacion3 = sueldo3 * 0.13 

"se suman las bonificaciones al sueldo"
sueldo_neto1 = sueldo1 + bonificacion1
sueldo_neto2 = sueldo2 + bonificacion2
sueldo_neto3 = sueldo3 + bonificacion3

"Evaluación de horas trabajadas y mensaje de sueldo según corresponda"
if horas_trabajadas > 120:
    print("Sueldo bruto: $", sueldo1)
    print("Bonificación del 18% por horas trabajadas: ", bonificacion1)
    print("Sueldo neto: ", sueldo_neto1) 
elif horas_trabajadas <= 120 and horas_trabajadas >= 80: 
    print("Sueldo bruto: $", sueldo2) 
    print("Bonificación del 15% por horas trabajadas: ", bonificacion2)
    print("Sueldo neto: ", sueldo_neto2) 
else:
    print("Sueldo bruto: $", sueldo3) 
    print("Bonificación del 13% por horas trabajadas: ", bonificacion3)
    print("Sueldo neto: ", sueldo_neto3) 