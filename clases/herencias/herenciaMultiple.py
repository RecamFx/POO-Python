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
        print(f"La habilidad es {self.habilidad}")


roberto = Empleado("Roberto",20,"Argentino","programador",100000) 

print(roberto.nombre) #? Roberto
roberto.hablar() #? Roberto esta hablando!