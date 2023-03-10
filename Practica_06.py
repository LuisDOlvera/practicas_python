
# Crea un programa para calcular el Perímetro de cualquier Polígono Regular
# Usa "While" para asegurarte de que los valores ingresados por el usuario son válidos. 

numero_lados = int(input("ingresa el numero de lados de un Polígono Regular: "))

while numero_lados < 3:
    print("Numero de lados incorrecto, ingresa un dato que sea válido:")
    numero_lados = int(input("ingresa el numero de lados de un Polígono Regular: "))

longitud = int(input("Ingresa la longitud de uno de los lados de Polígono Regular "))

while longitud <= 0:
    print("La longitud no puede ser menor o igual a 0, ingresa un dato que sea válido")
    longitud = int(input("Ingresa la longitud de uno de los lados de Polígono Regular"))

resultado = numero_lados * longitud

print("El resultado del Perímetro es: ", resultado)
          
