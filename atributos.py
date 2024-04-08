# Le sacamos los parentesis
class Celular:
    # Al crear una clase lo primero que se ejecuta es la funcion __init__
    # Self hacer referencia a si mismo (es como en vez de escribir celular.marca escribiesemos self.marca)
    def __init__(self, marca, modelo, camara): # A esta funcion se le llama funcion constructora o metodo constructor
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
celular1 = Celular("Samsung", "S23", "48MP") # Defino celulares
celular2 = Celular("Apple", "15 Pro Max", "38MP") # Defino celulares

print(celular1.marca) #? Samsung
print(celular2.marca) #? Apple