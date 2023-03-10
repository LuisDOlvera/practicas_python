#Variables y Tipos de Datos
#Podemos usar la función isinstance() para validar el tipo de dato

#int
x = 1
print(isinstance(x, int))

#float
average = 9.9
print(isinstance(average, float))

#str
name = "Pancho el Sancho"
print(isinstance(name, str))

#bool
is_awesome = True
is_boring = False

print(isinstance(is_awesome, bool))
print(isinstance(is_boring, bool))

#list
koders = ["Luis", "Daniel", "Manuel", "Sam", "Paola", "Toño"]
grades = [8, 9.9, 5, 1]

print(isinstance(koders, list))
print(isinstance(grades, list))

#El tipo None
#El valor None lo usamos para determinar explícitamente que no existe un valor

x = None
print(None)