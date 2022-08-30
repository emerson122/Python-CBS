# paradigmas de la programacion en python
class Persona:
    def __init__(self,nombre,edad,codigo):
        self.nombre = nombre #self se llama a si mismo
        self.edad = edad #self se llama a si mismo
        self.codigo = codigo #self se llama a si mismo
    

    def caminar(self):
        print("La persona ",self.nombre, " esta caminando.")
    

    def informacion(self):
        print(self.nombre," tiene la edad de ", self.edad)
    

persona1 = Persona("Sr. Mario Bros",21,'300001341254141241246') 
persona1.caminar()
print("y\n")
persona1.informacion()


