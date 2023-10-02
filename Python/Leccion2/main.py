# Comenzamos con funciones
# mi_funcion() # No se puede llamar antes de definir a una funcion
# definimos una funcion
def mi_funcion():  # Para identificar a la funcion utilizamos parentesis
    print("Saludos a todos los alumnos de la Tecnicatura")

mi_funcion() # Estamos llamando a la funcion
mi_funcion() # Se puede llamar a una funcion N cantidad de veces

#  Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name + " " + lastName)
persona = ["Franco", "Pagano"]
show(persona[0],persona[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*persona)  # Este es el mismo que el anterior pero le pasamos todo junto
persona2 = ("Oscar", "Pagano") # desempaquetamos a traves de una tupla
show(*persona2)
persona3 = {"name": "Franco", "lastName": "Pagano"}
show(**persona3)

number = [1, 2, 3, 4, 5]
for n in number:
    print(n)
    if n == 3:
        break # Esta es la unica manera de que no se ejecute el else
else:
    print("Esto se termino")

# List comprehension, lista de comprension
names = ["Paola", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "p"] # Este regresa una nueva lista
print(alongP)

buttleC = [{"name": "Quilnmes", "country" : "Arg"},
            {"name": "Corona", "country" : "Mx"},
            {"name": "Stella Artois", "country" : "Belgium"}
           ]
Arg = [b for b in buttleC if b["country"] == "Arg"]
print(Arg)
print(buttleC)

# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que ven a traves del canar de YouTube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Franco", "Pagano")

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a + b
# resultado = sumar(78, 22)
# print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(3,4)}")

def sumar2(a = 0, b = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f"El resultado de la suma es: {resultado}")

# Argumentos, variables en funciones
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listarNombres("Franco", "Juli", "Milo", "Bruno", "Pepe")

def listarTerminos(**terminos): # lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): # kwargs significa: key word argument
        print(f"{llave} : {valor}")

listarTerminos() # No recibe nada, anda se va a mostrar
listarTerminos(IDE = "Integrated Develoment Enviroment", PL = "Primaruy Key")
listarTerminos(Nombre="Franco Pagano")

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres2 = ["Titoi", "Pedor", "Carlos"]
desplegarNombres(nombres2)
desplegarNombres("Carla")
# desplegarNombres(10, 11) # No es iterable
desplegarNombres((10, 11)) # lo convertimos en tupla con dos elementos
desplegarNombres([22, 55]) # Lo convertimos en una lista

# Funciones Recursivas
def factorial(numero):
    if numero == 1: # Caso Base
        return 1
    else:
        return numero * factorial(numero -1) # Caso recursivo

resultado = factorial(5)
print(f"El factorial de 5 es: {resultado}")

