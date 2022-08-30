
# escriba un programa que pida tres numeros y 
# que escriba si son los tres iguales, si hay dos iguales o si los tres son distintos


#funcion para verificar numeros
def verificarnumeros(num1,num2,num3):
    if num1== num2  != num3 or num1 == num3 != num2 or num2 == num3 != num1:
        print("Has escrito uno de los numeros dos veces.")
    elif num1 == num2 == num3:
        print("Los 3 numeros son iguales")
    else :
        print("Los 3 numeros son diferentes")
    


#desarrollo del programa
print("\t\tCOMPARAR NUMEROS")
n1 = input("Escriba el primer numero:")
n2 = input("Escriba el segundo numero:")
n3 = input("Escriba el tercer numero:")



#envio de datos a la funcion
verificarnumeros(float(n1),float(n2),float(n3))