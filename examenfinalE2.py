# Crear un programa en Python donde se solicite N cantidad de numeros 
# (la cantidad que el usuario desse ingresar) y al terminar scar la mediana 
# de los numeros ingresados y mostrar el resultado en pantalla.

print("")
n = int(input("\t\tIngrese la cantidad de numeros a registrar: "))
suma = 0

i=1
while(i<=n):
    print("")
    print("Ingrese el dato ",i,)
    n2 = float(input())
    suma=suma+n2
    i+=1

mediana =suma/n

print("La mediana es:", mediana)
