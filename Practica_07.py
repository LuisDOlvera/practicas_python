# Crear un programa que imprima los números del 1 al 100.contador
# En cada número divisible  entre 3 imprima "Fizz" junto al número. 
# En cada número divisible entre 5  imprima "Buzz" junto al número-
# Que Imprima "FizzBuzz" si es divisible entre ambos.

contador = 1

while contador < 101:
    if contador % 3 == 0 and contador % 5 == 0:
        print("FizzBuzz", contador)
    elif contador % 3 == 0:
        print("Fizz", contador)
    elif contador % 5 == 0:
        print("Buzz", contador)    
    print("contador: ", contador)
    contador = contador + 1

