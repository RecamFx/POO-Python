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

d.hablar()

# Si le ponemos pass a D vamos a ver que ya no imprime desde D, va a pasar a B
# PRIORIDAD:
# D,B,C,A
# Porque la b?
# Porque es la primera que definimos en el atributo de la clase D