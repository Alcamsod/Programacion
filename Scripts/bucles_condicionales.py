# Bucles y condicionales
# Para operar con condiones, repetir pasos y demás podemos realizar bucles: Mientras, si, para... Los básicos
# Aqui introducimos también el bloque Try-except que es muy útil.

##################################
####### If - else - elif  ########
##################################

categorias = ["Base", "Pro", "Premium"]
categoria = input(" Introduce una categoria ")
if categoria == "Base":
    print("Has elegido la categoría Base")
elif categoria == "Pro":
    print("Has elegido la categoría Pro")
elif categoria == "Premium":
    print("Has elegido la categoriá Premium")
else:
    print("Categoria que no es ninguna de las elegidas")

# Esto es poco eficiente y se puede mejorar

if categoria in categorias:
    print(f"Has elegido la categoría {categoria}")
else:
    print("La categoría no es ninguna de las elegidas")

##################################
############ While ###############
##################################


# Ojo con los numeros y el while: Coma flotante

precio = 0.0
precio_limite = 1.0
pasos = 0

while pasos < 10:
    precio += 0.1
    print(f"Paso {pasos + 1}: Precio actual = {precio}")
    pasos += 1


##################################
############ For #################
##################################

# Bucle 'for' para una cantidad conocida de elementos o iteraciones

print(" Usando 'for' para una cuenta precisa ")
precios_correctos = 0
for _ in range(10):
    precios_correctos += 0.1
    
print(f"Precio final usando 'for': {precios_correctos}")

##################################
####### Try - except #############
##################################

# Control de errores y excepciones
# El bloque 'try-except' nos permite manejar errores de forma controlada para que el programa no se detenga.
while True:
    try:
        entrada = int(input("Introduce un número entero: "))
        print(f"Has introducido el número: {entrada}")
        break
    except ValueError:
        print("¡Error! La entrada no es un número entero. Inténtalo de nuevo.")
