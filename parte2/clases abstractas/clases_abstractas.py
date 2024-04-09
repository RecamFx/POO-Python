from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, genero, actividad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.actividad = actividad
    
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad}")

# Las clases abstractas no se pueden llamar por si mismas
# Se necesita crearle una implementacion, como Estudiante()

class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, actividad):
        super().__init__(nombre, edad, genero, actividad)
    
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")


class Trabajador(Persona):
    def __init__(self, nombre, edad, genero, actividad):
        super().__init__(nombre, edad, genero, actividad)
    
    def hacer_actividad(self):
        print(f"Trabajo en el rubro de: {self.actividad}")


stephen = Estudiante("Stephen", 36, "Masculino", "basquet")
stephenC = Trabajador("StephenC", 26, "Masculino", "basquet")

stephen.presentarse()
stephen.hacer_actividad()
stephenC.presentarse()
stephenC.hacer_actividad()