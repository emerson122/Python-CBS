# leer archivo

# texto = open('texto.txt','r')
# frase = texto.read()
# print(frase)


# Escribir archivo sin funcion
# txt = open('texto.txt','w')
# nombre = input("ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# txt.write(nombre + '\n')
# txt.write(apellido + '\n')
# txt.close()


# escribir archivo con funcion

def escribir_archivo(arg1,arg2):
    txt = open("texto.txt","w")
    txt.write(arg1 + '\n')
    txt.write(arg2 + '\n')
    txt.close()

nombre = input("ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
escribir_archivo(nombre,apellido)


# archivo-apendice.py anexar al archivo
# f = open('texto.txt','a')
# f.write('\n' + 'Hola Mundo')
# f.close()