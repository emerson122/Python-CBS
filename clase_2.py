# Concatenacion

from pickle import TRUE


nombre = "Luis"
apellido = "Perez"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

# MULTIPLICACION DE CADENAS DE TEXTO
animal = "perro"

print(animal*3)

# MULTIPLICACION DE CADENAS DE valores numericos enteros
edad = 3
print(edad*3)

# cantidad de caracteres
curso = "Fundamentos de programacion en python"
cantidad = len(curso)
# print(cantidad)

# anadir caracteres a una cadena
print("/////////////////////////////////////////////////////////////////")
curso2 = "Fundamentos"
print(curso2)
curso2 += " de"
print(curso2)
curso2 += " programacion"
print(curso2)
print("////////////////////////////////////////////////////////////////")

#busqueda de cadenas
frase = "unos puede leer Guerra y paz y creer que es un libro de aventuras mientas otros leer libro ...."
print(frase.find("paz"))
print(frase.find("libro"))

#confirmacion de la existencia de una subcadena
frase = "unos puede leer Guerra y paz y creer que es un libro de aventuras mientas otros leer libro ...."
x = print("Guerra" in frase)

print("existe:"+x)

#confirmacion de no existencia de una subcadna
print("confirmar que no existe:")
print("otros" not in frase)

#Conversiones de cadenas de mayusculas y minusculas
name = "angelthy"
Segundo_nombre = "LAURREN"

print(name.upper())
print(Segundo_nombre.lower)

#
num1 = 10
num2 = 35
#sumatoria
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)

#bloques de codigo
def concatenacion(arg1,arg2,nom_comp):
    print(arg1 +" " + arg2, nom_comp)


concatenacion(nombre,apellido + " Nombre Completo:", nombre_completo)