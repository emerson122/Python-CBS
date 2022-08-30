#utilizar un ciclo While debera crear un programa que haga un contador de 1 a 100 inidicadno lo siguiente
from multiprocessing.pool import IMapIterator


# si un numeros es impar indicar: x numero es impar 
# si un numero es par indiecar: x numero es par

def num_par_impar(n1):
    if (n1 % 2) == 0:
        print(n1," Es un numero par")
    else:
        print(n1," Es un numero impar")
i=1
while i <= 100:
    num_par_impar(i)
    i+=1