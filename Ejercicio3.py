# Elabore un programa que solicite al usuario dos numeros enteros 
# elprograma debera contener una funcion parqa sumar, otra funcion para dividir y otra para multiplicar
# cada funcion debe presentar en pantalla el resultado de la operacion entre ambos numeros


#funciones
def sumar(n1,n2):
    print("La suma es:", int(n1)+int(n2))

def resta(n1,n2):
    print("La Resta es:",int(n1)-int(n2))

def dividir(n1,n2):
    print("La division es:",int(n1)/int(n2))

def multiplicar(n1,n2):
    print("La multiplicacion es:",int(n1)*int(n2))

#desarrollo del programa
num1 = input("Ingrese un numero entero para realizar las operaciones")
num2 = input("Ingrese un segundo numero entero para realizar las operaciones")

sumar(num1,num2)
resta(num1,num2)
dividir(num1,num2)
multiplicar(num1,num2)
#fin del programa
