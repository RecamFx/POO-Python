# Con las propiedades podemos definir getters, setters y deletters

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self._edad = edad
        
    @property # Le decimos que es una propiedad
    def nombre(self): # En este caso un getter
        return self.__nombre
    
    @nombre.setter # Le decimos @ nombre de la funcion propiedad que es getter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
        
    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
stephen = Persona("Stephen", "36")

# Al decirle que es una propiedad no hace falta poner los parentesis
print(stephen.nombre) #? Stephen

stephen.nombre = "Lebron" # Modificamos usando el setter

print(stephen.nombre) #? Lebron


# Para eliminarlo, tenemos que crear la propiedad deleter
del stephen.nombre
# Si no, no saltaria error al eliminar