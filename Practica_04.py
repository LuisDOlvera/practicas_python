#Crear un programa que solicite un número al usuario e imprima en consola "par" si el numero es par o "impar" si el número es impar
#SI RESIDUO DE DIVIDIR ENTRE 2 ES CERO ES PAR, SI ES DIFERENTE DE CERO ES IMPAR

numero = float(input("Ingresa un número cualquiera: "))

residuo = numero % 2

if residuo == 0:
  print("Es número par")
if residuo != 0:
  print("Es numero Impar")