# Los setters y getters sirven para acceder a un atributo de una accion que sea privado
# Son conceptos

class Persona:
    def __init__(self, nombre, edad, edad2):
        self._nombre = nombre # Atributo privado
        self._edad = edad
        self.__edad2 = edad2 # Atributo muy privado
        
    def get_nombre(self):
        return self._nombre
    
    def get_edad2(self):
        return self.__edad2
    
    def set_edad(self, edad):
        self._edad = edad
    
stephen = Persona("Stephen", "36", "34")

print(stephen._nombre) # Esto esta mal #? Stephen
print(stephen.get_nombre()) # Esto es correcto #? Stephen


#!print(stephen.__edad2) # Esto esta mal #? ERROR
print(stephen.get_edad2()) # Esto es correcto #? Stephen



print(stephen._edad) #? 36
stephen.set_edad(20) # Cambiandome de nombre
print(stephen._edad) #? 20