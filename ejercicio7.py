# EJERCICIO 7: Del punto anterior, y considerando que durante 12 meses el empleado trabajó las mismas cantidades
# de horas, escribe un programa que calcule el descuento anual a realizarse, considerando: 
#  a. Si el sueldo anual es mayor a $2.000.000, el descuento es del %5.
#  b. Si el sueldo anual esta entre $1.000.000 y $2.000.000, debe aplicarse un descuento del %3.
#  c. Si el sueldo anual es menor a $1.000.000, debe aplicarse un descuento del %1. 
#  d. El programa debe mostrar el salario anual bruto, el monto anual de bonificaciones, el monto anual 
# a descontarse y las horas trabajadas en todo el año.

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
    print("Sueldo anual bruto: $", sueldo1 * 12) 
    print("Bonificación anual: $", bonificacion1 * 12) #Mensaje y cálculo de bonificación anual corresponiente.
    print("Descuento anual del 5%: $", (sueldo1 * 12) * 0.5) 
    print("Horas anuales trabajadas: ", horas_trabajadas * 12) 
elif horas_trabajadas <= 120 and horas_trabajadas >= 80: 
    print("Sueldo anual bruto: $", sueldo2 * 12) 
    print("Bonificación anual: $", bonificacion2 * 12) #Mensaje y cálculo de bonificación anual corresponiente.
    print("Descuento anual del 3% : $", (sueldo2 * 12 ) * 0.3)
    print("Horas anuales trabajadas: ", horas_trabajadas * 12) 
else:
    print("Sueldo anual bruto: $", sueldo3 * 12) 
    print("Bonificación anual: $", bonificacion3 * 12) 
    print("Descuento anual del 1%: $", (sueldo3 * 12) * 0.1) 
    print("Horas anuales trabajadas: ", horas_trabajadas * 12) 