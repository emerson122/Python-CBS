#Desarrollar un programa que solicite un numero al usuario con instrucciones detalladas. El program de ser capaz
# de realizar lo siguiente

                                # Evaluar si el numero ingresado es entero

# 1 si el numero es par indicar en pantalla que el numero es par
# 2 Si el numero es impar, indicar en pantalla que el numero es impar
# 3 Si el numero es impar y es multiplo de 3 indicarlo en pantalla de manera optima
# 4 si el numero es impar y es multplo de 5 indicarlo en pantalla
# 5 si el numero es imapr y es multiplo de 5 y de 3 indicarlo en pantalla



num1 = input("Ingresar un numero entero:")
while num1.isnumeric() != True:
    print("El valor ingresado debe ser un numero entero")
    num1 = input("Ingresar un numero entero:")


def multi3(n1):
    if n1 % 3 == 0:
        print(n1," Es un numero multiplo de 3")
    else:
        return False
def multi5(n1):
     if n1 % 5 == 0:
        print(n1," Es un numero multiplo de 5")
     else:
            return False

def ambos(n1):
    if(n1 % 3 and n1 % 5) == 0: 
        print(n1," Es un multiplo de 5 y de 3")
    else:
        return False

def num_par_impar(n1):
    if (n1 % 2) == 0:
        print(n1," Es un numero par")
    else:
        print(n1," Es un numero impar")
        multi3(int(n1))
        multi5(int(n1))
        ambos(int(n1)) 
        
        

num_par_impar(int(num1))