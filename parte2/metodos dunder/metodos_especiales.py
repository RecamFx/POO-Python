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
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre, nuevo_valor)

stephen = Persona("Stephen", 36)
pedro = Persona("Pedro", 30)
maria = Persona("Maria", 20)

print(stephen) #? Persona(nombre={self.nombre},edad={self.edad})

representacion = repr(stephen)
resultado = eval(representacion)

print(resultado) #? Persona(nombre=Stephen,edad=36)


nueva_persona = stephen + pedro + maria
print(nueva_persona)