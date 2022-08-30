#tuplas y cadenas python

# valores = (5,"Hola mundo",False,-2.45)
# print(len(valores))
# print(type(valores[2]))



from ast import For


numeros = [1,2,3,4,5,6]
print("lista antes del append:" , numeros )
numeros.append(7)
print("Lista despues del append:" + str(numeros) )

# insertar en las tuplas

alumnos = ["Jose","Abigail","Pablo"]
print(alumnos)
alumnos.insert(2,"Roberto")
print(alumnos)

#eliminar elementos de una lista
print(alumnos)
del alumnos[0]
print(alumnos)

# largo de un lista
print(len(alumnos)-1)

#Slicing
lenguajes = ["C","c++","Python","Perl","PHP","pascal"]
print(lenguajes[2:5])
print(numeros[0:4]) # indice 0 1 2 3

#Diccionarios
diccionario = {'Nombre': 'Emerson Ramos','Edad':21,'Cursos':['Python','Javascript',"Go"]}
print(diccionario['Edad']) #imprimir la edad del diccionario
print(diccionario['Cursos'][1]) #imprimir el indice 1 del diccionario

#interaciones
# for <elem> in <interable<:
#     <tu codigo>

valores = {'A':1,'B':2,"C":3}
for n in (numeros):
    print(n)

for k,y in valores.items():
    print("K=",k,"Y=",y)

n =1
y= 10
# for x in range(n,y): #de 1 a antes de 10
for x in range(n,y+1): # de 1 a 10
    print(x)
    input("Presione una tecla........")

preguntas = ["Ingrese sun nombre:", "Ingrese su apellido", "ingrese su edad:"]
respuestas = []
print("Respuestas:", respuestas)
for x in preguntas:
    respuestas.append(input(x))


print("Respuestas:", respuestas)