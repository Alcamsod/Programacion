import random
##################################
########### Funciones ############
##################################

# A la hora de realizar operaciones repetidas podemos crear las funciones, que nos sirve, como su nombre indica, para agrupar código y hacerlo reutizable.
# Las funciones pueden recibir parámetros o no, devolver valores o simplmemente ejecutar acciones.

# Función más básica con la tipología más correcta: Comentarios, tipo de retorno, etc.
def calcular_precio(precio_base, descuento) -> float:
    """
    Comentarios de la función
    """
    precio_final = precio_base - (precio_base * descuento / 100)
    return precio_final


#Ejecutar solo acciones

def elegir_cupon():
    """
    """
    precio = random.normalvariate(100, 20)
    print(f"Se ha elegido un precio aleatorio: {precio} €")


# Llamamos a las funciones por ejemplo

elegir_cupon()

precio_final = calcular_precio(100, 15)
print(f"El precio final es: {precio_final} € ")