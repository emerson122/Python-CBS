#Declarar variables
name = "Emerson Exequiel Ramos Velasquez" 
edad = 21
asignacion = "Informatica"
pi =  3.141592653589793238462
#extra funcion para calcular pi
def Calcularpi(n):
    num = ((-1)**n)/((2*n)+1)
    return num

pi2 = 0
#fin de extra
numerodecuenta = 20191004510



#Desarrollo del programa
print("")
print("/////////////////////////////////////////////////////////////////////////")

print("\tNombre del estudiante: " +  name+"\t      //" )
print("\tEdad:                 ", edad,"\t\t\t\t     //")
print("\tAsignacion:            "+asignacion +"\t\t\t    //")
print("\tNumero PI:            ", pi,"\t\t   //")
#Calculo extra de Pi
for i in range(10000):
    pi2 = pi2 + Calcularpi(i)
print("\tCalculo de pi:        ", pi2*4, "\t\t  //")
print("\tDPI:                  ", numerodecuenta , "\t\t\t //")
print("//////////////////////////////////////////////////////////////////")
print("")

#fin del programa