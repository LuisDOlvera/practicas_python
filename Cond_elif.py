

edad = 38
nacionalidad = "alemana"
tiene_permiso = "True"
es_mayor_de_edad = edad >= 18

if edad >= 18 and nacionalidad == "mexicana":
    print("Tome su cerveza buen hombre")
elif edad >= 21 and nacionalidad == "gringo":
    print("Enjoy your beer luky man") 
elif edad >= 15 and nacionalidad == "alemana":
    print("Toma tu cerveza alemana")
else:
    print("A la cabaña de los pequeñines")    
if edad >= 18 or tiene_permiso:
    print("Puede conducir")      
if es_mayor_de_edad:
    print("es mayor de edad")    
