# Los decoradores como dice su nombre decoran funciones
# Toman una funcion de entrada y le agregan una funcionalidad (decoracion)

# Los decoradores pueden ser como validaciones
# EJEMPLO: Para abrir una puerta, haces una funcion que abra la puerta, pero con el decorador le decis que si son las 9 de la manana que no le de importancia

def decorador(funcion):
    def funcion_modificada():
        print("Antes de la funcion!")
        funcion()
        print("Despues de la funcion!")
    return funcion_modificada



# def saludo():
#     print("Hola Stephen!")
    
    
# # Para ejecutar una funcion modificada necesitamos ponerla en una variable

# func_modificada = decorador(saludo) # La funcion en parametro debe ir sin parentesis

# func_modificada() # La ejecutamos

#? Antes de la funcion!
#? Hola Stephen!
#? Despues de la funcion!


#todo MANERA OPTIMA DE HACERLO

@decorador # Decora automaticamente la funcion
def saludo():
    print("Hola Stephen!")
    
saludo()

#? Antes de la funcion!
#? Hola Stephen!
#? Despues de la funcion!