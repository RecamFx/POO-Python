# Para usar herencia vamos a crear una clase comun llamada persona, que es todo lo que es una persona
# Y despues una clase para cada persona en particular, pero vamos a hacer que todas las personas hereden las mismas caracteristicas pero con algunas cosas diferentes

class Persona:
    def __init__(self, nombre, edad , nacionalidad):
        self.nombre = nombre 
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f"{self.nombre} esta hablando!")
        
        
class Empleado(Persona): # Si entre los parentesis le ponemos otra clase, esa misma clase va a heredar los atributos de la otra
    # Agregamos mas atributos de los que ya tenia
    def __init__(self, nombre, edad , nacionalidad, trabajo, salario): # Le ponemos todos los atributos que queremos que tenga
        super().__init__(nombre, edad , nacionalidad) # Aca le decimos que queremos que herede
        self.trabajo = trabajo
        self.salario = salario
    #pass # Pass funciona para crear algo pero no sabemo que va definir


roberto = Empleado("Roberto",20,"Argentino","programador",100000) # Le pasamos a empleado los atributos


print(roberto.nombre) #? Roberto
roberto.hablar() #? Roberto esta hablando!