# Crear un programa que solicite al usuario la siguiente información:

# - Nombre del alumno
# - Número de identificación del alumno
# - Nota final de la asignación de Física 1
# - Nota final de la asignación de Programación 1

# - Nota final de la asignación de Estadística

# - Nota final de la asignación de Electrónica Analógica

# Cada uno de estos inputs deberán asignarlos a una sola variable del tipo lista en el orden especificado.
# Presentarán al usuario un resumen ordenado de toda la información que ingresó y le informará cuál es el promedio
# obtenido de todas las asignaciones solicitadas.
preguntas = ["Nombre de Alumno: ", "Nombre de indentificacion del alumno: ","Nota final de la asignación de Física 1: ", "Nota final de la asignación de Programación 1: ","Nota final de la asignacion de estadistica: ","Nota final de la asignacion de electronica Analogica: "]

resumen = ['Nombre:' ,'identificacion:','Notas finales:']
print("\tRegistro de Calificaciones")
print("\t      __...--~~~~~-._   _.-~~~~~--...__")
print("\t    //               `V'               \\")
print("\t   //                 |                 \\")
print("\t  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\ ")
print("\t //__.....----~~~~._\ | /_.~~~~----.....__\\")
print("\t====================\\|//====================")
print("\t                erv `---`")

respuestas = []
for x in preguntas:
    respuestas.append(input(x))

# print(respuestas[1])
print("")
print("=================================Resumen================")
n=0
def sacarpromedio(n1,n2,n3,n4):
    respuesta= int(n1)+int(n2)+int(n3)+int(n4)
    respuestaf = respuesta/4
    return respuestaf

for n in range(n,1):
    print(resumen[n],respuestas[n])
    print(resumen[n+1],respuestas[n+1])
    print("////////////////////////////////////////////////////////////////////////")
    print("\t"+ resumen[n+2],"\n\t\t\t",respuestas[n+2],"\n\t\t\t",respuestas[n+3],"\n\t\t\t",respuestas[n+4],"\n\t\t\t",respuestas[n+5])
    print("Promedio Final: ",sacarpromedio(respuestas[n+2],respuestas[n+3],respuestas[n+4],respuestas[n+5]))