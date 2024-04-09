class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Los metodos especiales son metodos guionados dos veces
    # El metodo str nos permite devolver esta clase como una cadena de texto
    def __str__(self):
        return f'Persona(nombre={self.nombre},edad={self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}",{self.edad})'

stephen = Persona("Stephen", 36)

print(stephen) #? Persona(nombre={self.nombre},edad={self.edad})

representacion = repr(stephen)
resultado = eval(representacion)

print(resultado) #? Persona(nombre=Stephen,edad=36)