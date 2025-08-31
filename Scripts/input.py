# En python no es necesario declarar las variables, es decir
nombre = input("¿Como te llamas?: \n")
edad = input("Cuántos años tienes?: \n")
print(f"Hola, ¿qué tal estas {nombre}?")
print(f"Veo que tienes {edad} años")
print(type(nombre))
print(type(edad))

# Podemos sin embargo realizar las declaraciones para evitar problemas
nombre_str: str = input("¿Como te llamas?: \n")
edad_int: int = input("Cuántos años tienes?: \n")
print(f"Hola, ¿qué tal estas {nombre_str}?")
print(f"Veo que tienes {edad_int} años")
print(type(nombre_str))
print(type(edad_int))

##################################
####### Resto de variables #######
##################################

# Strings: Son cadenas de texto, se puede operar con ellos como si fueran "numeros"
print(nombre + " tiene " + edad + " años")
# De hecho si intentamos hacer la suma entre tipos falla
try:
    print(nombre + " tiene " + edad + " años")
except: 
    print("❌ He fallado, tengo que hacer cambio de variable ")
    print(nombre + " tiene " + str(edad) + " años")

#Bool: True or false: Dicotomico.
existe: bool = True

if existe:
    print("La variable existe")
else:
    print("La variable no existe")

# Arrays
nombres = ["Aisa", "Natalia", "Alberto"]
# Con los arrays podemos hacer operaciones como ordenarlos, filtrar etc.
nombres.sort(key=lambda x: x.lower())
print(nombres)
nombres.sort(key=lambda x: len(x))
print(nombres)

# Tuple
tupla: tuple = (nombre_str, edad_int, existe)
# No podemos operar pero si acceder a ellos
print(tupla[0])
print(tupla[1])
print(tupla[2])

# Dict: No sirve para crear por ejemplo registros
registro: dict = {
    "nombre": nombre_str,
    "edad": edad_int,
    "existe": existe,
}