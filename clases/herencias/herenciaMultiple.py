# Heredar mas de una clase

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
    def __init__(self, nombre, edad , nacionalidad, habilidad, salario, empresa): # Tod0s los atributos que quiere eredar
        Persona.__init__(self, nombre, edad , nacionalidad) # De persona
        Artista.__init__(self, habilidad) # De artista
        
        self.salario = salario
        self.empresa = empresa
        self.habilidad = habilidad
        
    def mostrar_habilidad(self): # Creamos esta funcion para demostrar lo que hace super()
        return "No tengo jaja"
        
    def presentare(self):
        return f"{self.mostrar_habilidad()}", f"{super().mostrar_habilidad()}" 
        # Super() seria mas correcto, ya que le decimos al programa que es una herencia
        # Si ponemos self, va a buscar en la misma clase y despues en las clases herederas
        # Super() directamente busca en las clases herederas
        
        # Por eso nos da 2 resultados diferentes

roberto = EmpleadoArtista("Roberto",20,"Argentino","Cantar",100000,"ProgramingInc") 

print(roberto.nombre) #? Roberto
print(roberto.presentare()[0]) #? No tengo jaja
print(roberto.presentare()[1]) #? La habilidad es Cantar