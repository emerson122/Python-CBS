#Operadores Relacionales
# 4 == 7
# 5 != 6
# 'hola' == 'hola'
# 'hola' != 'hola'
# 5<8
# 5>8
# 5<=8
# 5>=8


# operadores aritmeticos
# + suma
# - resta
# / division
# % realiza una division de 16 entre 3 y nos da el residuo (si es 1 es impar si es 2 es par)
# ** realiza la potenca de los operados 12** 3 = 1728

# // realiza la division con resultado de numero entero 18//5 = 3
password= "qwerty"
pass_ingresado = input('ingrese password> ')

if pass_ingresado == password:
    print('password incorrecto. Bienvenido Crack')
else:
    print('passsword incorrecto. Vuelve a intentarlo')


palabra= 'bici'
palabra1 = 'moto'
palabra2 = 'bici'
palabra3 = 'patin'

if palabra == palabra1:
    print(palabra + ' es igual a '+ palabra1)
elif palabra == palabra2:
    print(palabra + ' es igual a '+ palabra2)
elif palabra == palabra3:
    print(palabra + ' es igual a '+ palabra3)
else:
    print("nada es correcto Crack, vuelve a intentarlo")

