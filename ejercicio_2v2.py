
#Desarrollo del programa
print("\t\t\t\t\t\t\t       )  ( ")
print("\t\t\t\t\t\t\t      (   ) )")    
print("\t\t\t\t\t\t\t       ) ( (")     
print("\t\t\t\t\t\t\t    __)_____)_")
print("\t\t\t\t\t\t\t .-'---------| ") 
print("\t\t\t\t\t\t\t( C|/\/\/\/\/|")
print("\t\t\t\t\t\t\t '-./\/\/\/\/|")
print("\t\t\t\t\t\t\t   '_________'")
print("\t\t\t\t\t\t\t    '-------'")

print("\t\t\t\t\t\t█▀▀ ▄▀█ █▀▀ █▀▀ ▀█▀ █▀▀ █▀█ █ ▄▀█")
print("\t\t\t\t\t\t█▄▄ █▀█ █▀░ ██▄ ░█░ ██▄ █▀▄ █ █▀█")
name = input("Ingresa el nombre del cliente: ")
nui = input("Favor ingrese el numero de indentificacion del cliente: ")
pd1 = input("Ingrese el nombre del producto 1: ")
costo1 = input("Valor del producto>")
print("------------------------------------------------------------")
pd2 = input("Ingrese el nombre del producto 2: ")
costo2 = input("Valor del producto>")
print("------------------------------------------------------------")
pd3 = input("Ingrese el nombre del producto 3: ")
costo3 = input("Valor del producto>")
print("")
print("/////////////////////////////////////////////////////////////////////////")
print("\tNombre cliente:\t"+ name)
print("")
print("\tNo. indetificacion:\t",nui)
print("")
print("\tProductos comprados:\t\n\t\t"+ pd1+":\t"+ costo1 +"\n\t\t" + pd2 +":\t" + costo2 + "\n\t\t" + pd3 + ":\t" + costo3 + "\n\t\t")
print("\tTotal a pagar es L.",int(costo1)+int(costo2)+int(costo3))
print("/////////////////////////////////////////////////////////////////////////")

#fin del desarrollo del programa

