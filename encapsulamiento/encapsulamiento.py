# En python no funciona bien

class MiClase:
    def __init__(self):
        self._atributo_privado = "valor"
        self.__atributo_muy_privado = "valor"

objeto = MiClase()
print(objeto._atributo_privado)
print(objeto.__atributo_muy_privado)