# Los decoradores como dice su nombre decoran funciones
# Toman una funcion de entrada y le agregan una funcionalidad (decoracion)

def decorador(funcion):
    def funcion_modificada():
        print("Antes de la funcion!")
        funcion()
        print("Despues de la funcion!")
    return funcion_modificada

def saludo():
    print("Hola Stephen!")
    
    
# Para ejecutar una funcion modificada necesitamos ponerla en una variable

func_modificada = decorador(saludo) # La funcion en parametro debe ir sin parentesis

func_modificada() # La ejecutamos