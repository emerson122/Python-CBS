# la funcion factorial es una formula matematica representada por el signo de exclamacio "!" en la formula factorial se deben
# multiplicar todos los numeros enteros y positivos que hay entre el numero que aparecen en la formula y el numero 1
#  crear un programa que solicite un numero al usuario y se le devuelva el resultado de la formula factorial

numero = int(input("Numero: "))
factorial = 1
if numero  !=0:
    for i in range(1,numero+1):
        factorial = factorial*i

print("Factorial",factorial)