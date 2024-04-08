# MRO o Method resolution order

class Persona:
    def __init__(self, nombre, edad , nacionalidad):
        self.nombre = nombre 
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f"{self.nombre} esta hablando!")

        
class Empleado(Persona):
    def __init__(self, nombre, edad , nacionalidad, trabajo, salario):
        super().__init__(nombre, edad , nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f"La habilidad es {self.habilidad}"



class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad , nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad , nacionalidad)
        Artista.__init__(self, habilidad)
        
        self.salario = salario
        self.empresa = empresa
        self.habilidad = habilidad
        
    def mostrar_habilidad(self): # Creamos esta funcion para demostrar lo que hace super()
        return "No tengo jaja"
        
    def presentare(self):
        return f"{super().mostrar_habilidad()}"

roberto = EmpleadoArtista("Roberto",20,"Argentino","Cantar",100000,"ProgramingInc") 

print(roberto.nombre) #? Roberto
print(roberto.presentare()) #? La habilidad es Cantar