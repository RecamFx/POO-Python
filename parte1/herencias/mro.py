# MRO o Method resolution order

class A:
    def hablar(self):
        print("Hablando desde A")
        
class F:
    def hablar(self):
        print("Hablando desde F")
        
class B(A):
    def hablar(self):
        print("Hablando desde B")
        
class C(F):
    def hablar(self):
        print("Hablando desde C")
        
class D(B,C):
    pass
    # def hablar(self):
    #     print("Hablando desde D")

        
d = D()

d.hablar() #? Hablando desde B

print(D.mro()) #? [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class '__main__.F'>, <class 'object'>]
# Usando el metodo .mro() podemos ver el orden en el que se ejecutan las clases

# Si le ponemos pass a D vamos a ver que ya no imprime desde D, va a pasar a B
# PRIORIDAD:
# D,B,C,A
# Porque la b?
# Porque es la primera que definimos en el atributo de la clase D