# ejercicio 3: Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla.
# El programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar).

"se le pide al usuario que ingrese el valor del dolar "
dolar = float(input("Ingrese el valor del dolar al dia de hoy: "))
dolar_a_convertir = float(input("Ingrese la cantidad de dólares a convertir en pesos argentinos: ")) 
"Cálculo de conversión de dólares a pesos"
dolarcambio = dolar * dolar_a_convertir 
"se muestra la equivalencia"
print("la cantidad de :",dolar_a_convertir , "dolares, serian:", dolarcambio)