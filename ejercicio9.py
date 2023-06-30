# EJERCICIO 9: Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad
# de personas ingresada por el usuario.


"empezamos el programa"
print("A continuación, ingresar nombre, apellido y edad de una persona")

continuamos = 1 #variable para determinar si agregar mas personas o no

while continuamos == 1 : 
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad:"))
    
    print ("Nombre: ", nombre, " Apeliido: ", apellido, " Edad: ", edad) #se muestran los datos
    continuamos = int(input("¿Continuamos? 1.si / 2.no: ")) 

