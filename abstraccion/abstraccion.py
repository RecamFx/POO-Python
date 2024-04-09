# Abstraccion es cuando el usuario no sabe que hacemos en el codigo, es como:
# Saber manejar un auto pero no saber como se mueve el motor para dar la fuerza de empuje

# Es como ocultar la complejidad de un sistema

# Aca lo mismo, el usuario conduce el auto pero no sabe que estamos checkeando que el auto este encendido

class Auto():
    def __init__(self):
        self.estado = "apagado"
        
    def encender(self):
        self.estado = "encendido"
        print("Auto encendido")
        
    def conducir(self):
        if self.estado == "apagado":
            self.encender()
        print("Conduciendo el auto")


miAuto = Auto()

miAuto.conducir()