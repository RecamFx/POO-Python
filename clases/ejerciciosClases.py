# EJERCICIO:
# Crear una clase estudiante
# Que tenga atributos nombre, edad y grado
# Agregar un metodo estudiar() que diga "El estudiante (nombre) esta estudiando"
# Ademas que el usuario tenga que rellenar los datos desde la consola

# Respuesta:

class Estudiantes:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiando(self):
        print(f"El estudiante {self.nombre} esta estudiando")
        
nombre = input("Nombre: ")
edad = input("Edad: ")
grado = input("Grado: ")

estudiante = Estudiantes(nombre, edad, grado)

while True:
    respuesta = input("").lower()
    print(respuesta)
    if respuesta == "estudiar":
        estudiante.estudiando()