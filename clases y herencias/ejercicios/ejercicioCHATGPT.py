# EJERCICIO:
# Hacer una clase que obtenga los datos de un rectangulo y tenga atributos de largo y ancho, y que haya dos modulos que calculen el area y perimetro
# Que el usuario tenga que ingresar el largo y ancho

class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        
    def area(self):
        return self.largo * self.ancho 
    
    def perimetro(self):
        return self.largo*2 + self.ancho*2
    
while True:
    try:
        largo = int(input("Ingresa el largo: "))
        ancho = int(input("Ingresa el ancho: "))
        
        dato = Rectangulo(largo, ancho)
        
        print(f"""Datos del rectangulo:
    Largo = {dato.largo}
    Ancho = {dato.ancho}
    Area = {dato.area()}
    Perimetro = {dato.perimetro()}
    """)

    except:
        print("Datos invalidos!!")