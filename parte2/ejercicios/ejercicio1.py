# Crear personajes que puedan fusionarse

class Personajes:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f'{self.nombre}(Fuerza: {self.fuerza}, Velocidad: {self.velocidad})'
    
    def __add__(self, otro):
        nuevoNombre = self.nombre + "-" + otro.nombre
        nuevaFuerza = self.fuerza + otro.fuerza
        nuevaVelocidad = self.velocidad + otro.velocidad
        return Personajes(nuevoNombre, nuevaFuerza, nuevaVelocidad
)

Stephen = Personajes("Stephen", 70, 40)
Lebron = Personajes("Lebron", 63, 30)
Messi = Personajes("Messi", 90, 60)

print(Stephen + Messi)