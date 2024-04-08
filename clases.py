# Clases
# Para nombrar clases se recomienda usar PascalCase (Todas las primeras letras en mayusculas)

class Celular():
    marca = "Samsung"
    modelo = "S23"
    camara = "48MP"


celular1 = Celular()
print(celular1) #? <__main__.Celular object at 0x00000151AE626B10>


# Podemos acceder a los datos llamando a la clase y a la variable
print(celular1.camara) #? 48MP