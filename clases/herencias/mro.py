# MRO o Method resolution order

class A:
    def hablar(self):
        print("Hablando desde A")
        
class B(A):
    def hablar(self):
        print("Hablando desde B")
        
class C(A):
    def hablar(self):
        print("Hablando desde C")
        
class D(B,C):
    def hablar(self):
        print("Hablando desde D")
        
d = D()
d.hablar()