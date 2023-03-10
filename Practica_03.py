
#Crear un programa que solicite al usuario un número y le imprima la siguiente información:
# El doble del número.
# La mitad del número.
# La diferencia entre ese número y el número 100.
# El residuo de dividir ese número entre 3.
# No enfocarse en validaciones por el momento, asumir que el usuario ingresa un valor numérico.

numero = int(input("Ingresa un Número Cualquiera: "))

doble_num = numero * 2
mitad_num = numero / 2
dif_num = 100 - numero
res_num = numero % 3

print("El doble del número es: ", doble_num)
print("La mitad del número es: ", mitad_num)
print("La diferencia entre ese numero y el 100 es: ", dif_num)
print("El residuo del número es: ", res_num)