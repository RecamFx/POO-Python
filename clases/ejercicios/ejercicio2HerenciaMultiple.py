# Ejercicio de herencia múltiple y MRO:
# Imagina que estás modelando animales en un zoológico. 
# Crear tres clases: "Animal", "Mamifero" у "Ave". 
# La clase "Animal" debe tener un método llamado "comer". 
# La clase "Mamifero" debe tener un método llamado "amamantar" y la clase "Ave" un método llamado "volar".
# Ahora, crea una clase "Murcielago" que herede de "Mamifero" y "Ave", en ese orden, y por lo tanto debe ser capaz de "amamantar" y "volar", además de "comer".
# Finalmente, juega con el orden de herencia de la clase "Murcielago" y observa cómo cambia el MRO y el comportamiento de los métodos al usar super().


# Respuesta:

class Animal:
    def comer(self):
        print("Comiendo...")
        
class Ave(Animal):
    def volar(self):
        print("Volando...")
        
class Mamifero(Animal):
    def amamantar(self):
        print("Amamantando...")
        

class Murcielago(Mamifero, Ave):
    pass

murci = Murcielago()

murci.comer() #? Comiendo...

print(Murcielago.mro()) #? [<class '__main__.Murcielago'>, <class '__main__.Mamifero'>, <class '__main__.Ave'>, <class '__main__.Animal'>, <class 'object'>]