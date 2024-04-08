class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    # Si una funcion se coloca dentro de una clase, pasa a llamarse metodo (Ya no es mas una funcion)
    
    def llamar(self):
        print(f"Estas llamando desde un {self.modelo}")
        
    def cortar(self):
        print(f"Cortaste la llamada desde un {self.modelo}")
        
celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "15 Pro Max", "38MP")

celular1.llamar() #? Estas llamando desde un S23