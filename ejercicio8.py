# ejercicio 8: Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas.

personas = 0 #contador
"se piden los datos de 5 personas "
print("Ingresa el nombre, apellido y edad de cinco personas")
while personas < 5: 
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    "suma de a 1 las personas ingresadas" 
    personas = personas + 1 
    print("Persona ingresada numero ", personas , " Nombre: ", nombre, " Apellido: ", apellido, " . Edad: ", edad ) 