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