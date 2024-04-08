# El polimorfismo se basa en dar la misma accion a diferentes elementos y recivir diferentes respuestas
# Misma accion, diferente respuesta

class Gato():
    def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

# Dos tipos de polimorfismo:
hacer_sonido(gato) #? Miau
print(perro.sonido()) #? Guau