
numero = 10
edad = 38
nacionalidad = "mexicana"

if numero > 5:
    print(numero, "Es mayor a ", 5)
    
#Esta línea se ejecuta debido a que no es parte del bloque condicional y no está identado.
print("Esto se ejecuta sin importar la condición")    

if edad >= 18:
    print("puedes entrar al Bar")

if not edad >=18:
    print("No puedes entrar al Bar, regresa al kinder")

if edad < 18:
    print("Regresa al kinder")

if edad >= 18 and nacionalidad == "mexicana":
    print("Tome su cerveza buen hombre")    
