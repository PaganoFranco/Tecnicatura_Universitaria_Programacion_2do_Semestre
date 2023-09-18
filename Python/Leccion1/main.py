# lista = Elemento1, Elemento2, Elemento3, Elemento4
"""
COLECCIONES EN PYTHON (LISTA o ARREGLO o VECTORES)
Al crear una lista, los elementos toman posiciones como elementos de un conjunto.
"""
nombres = ["Elemento1", "Elemento2", "Elemento3", "Elemento4"]
print(nombres)
"""
Para recorrer del primer elemento al ultimo:
"""
print(nombres[0])  # Podemos visualizar un elemento en espesifico de la lista
print(nombres[1])
print(nombres[2])
print(nombres[-1])  # podemos visualizar el ultimo elemento, sin saber cual es
"""
Para recorrer del ultimo  elemento al primero:
"""
print(nombres[-1])
print(nombres[-2])
print(nombres[-3])

# -----------------------------------------------------------------------
nombres = ["Elemento1", "Elemento2", "Elemento3", "Elemento4"]
print(nombres)
print(nombres[0:2])  # Podemos visualizar los elementos dentro del rango nombres[0] y nombres[1]
print(nombres[:3])  # Podemos visualizar desde el primer elemento hasta el nombres[2]
print(nombres[1:])  # Podemos visualizar desde el nombres[1] hasta el ultimo

# Modificar un valor dentro de la lista
nombres[3] = "ElementoX"
print(nombres)

#Iterar una lista
for nombre in nombres: #nombre es singular, la lista plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

#-----------------------------------------------------------------------
# Preguntarnos cuantos elementos tiene
print(len(nombres)) # Len determina la cantidad de elementos del parametro (la lista)

# Agregamos un elemento
nombres.append("ElementoS")
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append([10.45])
nombres.append([4, 5])
nombres.append(7)
print(nombres)
# Una lista puede tener diferente tipos de elementos

# insertar un elemento en un indice espesifico
nombres.insert(1, "ElementoA") #Se agrega el elemento en dicha posicion, pero desplaza los demas a la derecha
print(nombres)
nombres.insert(2, "ElementoB")
print(nombres)

# Eliminar un elemento
nombres.remove("ElementoA") #Se elimina el elemento y se desplazan los siguiente a la izquierda
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[1] # "del" de DELETE
print(nombres)

# Eleminar/borar/limpiar todos los elemtnos
nombres.clear()
print(nombres)
"""
# Eliminar la lista
del nombres
print(nombres)
"""
#------------------------------------------------------------------
"""
Ejericio N°1: Iterar un rango de 0 a 10 pero imprimir numeros divisibles entre 3.
Ejemplo 0, 3, 6, 9 
"""
print("Rango de 0 a 10 con numeros divisibles entre 3")
#Segun yo
for i in range(10): #El erro es que un range(10) va del 0 al 9
    if i % 3 == 0:
        print(i)
#Segun video
for i in range(11):
    if i % 3 == 0:
        print(i)
"""
Ejercicio N°2: Crear un rango de numeros de 2 a 6 e imprimirlos
Ejemplo: 2, 3, 4, 5, 6
"""
print("Rango con valores de inicio = 2 y fin = 6")
# Segun yo
for x in range(7):
    if x > 1 :
        print(x)
#Segun video
rango = range(2, 7)
for i in rango:
    print(i)
"""
Ejercicio N°3: Iterar un rango de 3 a 10 pero con incremento de 2 en 2 en 
lugar de 1 en 1. Ejemplo 3, 5, 7, 9
"""
# Segun yo
rango = range(3, 11)
for y in rango:
    if y % 2 != 0:
        print(y)
# Segun video
print("El rango de inicio 3 y fin 10")
for i in range(3, 11, 2):
    print(i)

#-----------------------------------------------------------------------

# Definimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina)
print(len(cocina)) #Contamos la cantidad de elementos

# Acceder a un elemento (debemos usar corchetes y no parentesis).
print(cocina[0]) #Del primero al ultimo
print(cocina[-1]) #Del ultimo al primero

# Acceder a un rango
print(cocina[0:2])

# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar) # esta usando \n para saltos de linea

for cocinar in cocina:
    print(cocinar, end= " ") # Elimina los saltos de linea

# MODIFICAR UNA TUPLA
# cocina[0] = "plato" //Recordar que esto no se puede
# convertir de tupla a lista // Para poder modificarla
cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
# Convertir de lista a tupla
cocina = tuple(cocinaLista)
print("\n",cocina)

#---------------------------------------------------------------------

# Ejercicio de tupla: Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8) # Definimos la tupla
"""
Crear una lista que solo incluya los numeros menores a 5
e imrpima por consola [1, 3, 2]
"""

lista = [] # Definimos una lista vacia
# Filtramos los elemenetos menores a 5 de la tupla
for numero in tupla:
    if numero < 5:
        lista.append(numero)
print(f"La nueva lista es: {lista}")

#------------------------------------------------------
# Tipo set (conjunto)
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
print(len(planetas)) #Usamos la guncion len = length significa largo

# Revisamos si un elemento existe dentor de un set
print("Marte" in planetas) #El elemento a buscar debe escribirse igual al de la lista

# Revisamos si no existe un elemento dentro de un ser
print("Saturno" not in planetas)

# Agregar un elemento
planetas.add("Tierra")
print(planetas)

# Eliminar elementos
planetas.remove("Jupiter") # Puede arrojar error si el elemento no esta en la lista
print(planetas)

planetas.discard("Tierra")
print(planetas)

# limpiar set
planetas.clear()
print(planetas)

#Eliminar set o conjunto
"""
del planetas
print(planetas)
"""
# ---------------------------------------------------------------------------
# DICCIONARIO
# "Maradora":10 un diccionario esta compuesto de dos elementos asociados
# Una LLAVE y un VALOR
# dict{key, value}
diccionario = {
    "IDE" : "Integrate Development Eviroment",
    "POO" : "Programacion Orientada a Objetos",
    "SABD": "Sistema de adminitracion de Base de datos"
}
print(diccionario)
print(len(diccionario))

# Acceder a un diccionario con la llave(KEY)
print(diccionario["IDE"])

# Otra forma de recuperar un elemento
print(diccionario.get("POO"))
print(diccionario.get("SABD"))

#Modificamos elementos
diccionario["IDE"] = "Entorno de desarrollo Integrado"
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:
    print(termino) # Solo accedemos a las llaves

# Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino, valor) # Accedemos a las llaves y al valor

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): # Estamos usando una funcion KEYS
    print(termino) # Muestra solo las llaves

for valor in diccionario.values():  # Usamos una fucnion para acceder el valor
        print(valor)  # visualiza los valores sin llaves

print("IDE" in diccionario) # Devuelve un booleano

# Comprobar la existencia de algun elemento

# Agregar un elemento
diccionario["PK"] = "Primary Key"
print(diccionario)

# Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# Eliminar todos los elementos
diccionario.clear()
print(diccionario)
"""
# Eliminar diccionario
del diccionario # el diccionario se borro
"""

# Concatenamos listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7, 8, 9, 1]) # Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # la funcion index nos indica el indice de su posicion en la lista
# print(lista3.index(0)) # esto daria un error por no ser el elemento parte de la lista

# como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) # cuenta cuantos valores iguales hay dentro de la lista

# Para que una lista se multiplique repitiendo sus elementos
lista = [1, 2, 3] * 2
print(lista)

# Metodo de ordenamiento
lista3.sort()
print(lista3)
lista3.sort(reverse=True)
print(lista3)

# Repaso tuplas
tupla = (4, "hola", 6.3, [1, 2, 78], 4, "hola")
print(tupla)

print(4 in tupla) # Buscar un elemento

# Repaso de set o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {"bye", }
conjunto2.add(7)
conjunto2.add("hola")
print(conjunto2)
conjunto1.add("hola")
print(conjunto1)
print(3 not in conjunto1) # Preguntamos is el numero 3 NO esta en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Nos devuelve como respuesta un booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elementos tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # elementos que no comparten
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Verifica si el conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Verifica si los elementos del conjunto1 estan dentro del 3
print(conjunto2.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto 3 es subconjunto
print(conjunto2.issuperset(conjunto3))

# Verificar si ambos conjuntos son disconexos, esto es si comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) #No poseen elementos en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar, eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {"Azul" : "Blue", "Rojo" : "Red", "Amarillo": "Yellow"}
print(diccionarioNuevo)

# Como eliminar
del(diccionarioNuevo["Azul"])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {"Ariel": {"Edad":40, "Altura":1.83}, "Osvaldo":[45,1.85], "Natalia":[35,1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 Millones", "Posicion": "Extremo derecho"},
    11: {"Nombre": "Angel Di Maria", "Edad": 34, "Altura": 1.80, "Precio": "17 Millones", "Posicion": "Extremo derecho"},
    24: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 Millones", "Posicion": "Media punta"},
    19: {"Nombre": "Nicolas Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "3.5 Millones", "Posicion": "Defensa Central"},
    1: {"Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 Millones", "Posicion": "Portero"}
}

for llave, valor in seleccionArgentina.items():
    print(llave,valor)
# Como tarea agregar por lo menos 4 jugadores mas al diccionario: seleccionArgentina
print("Tenemos cargados en el diccionario una cantidad de jugadores: ", end=" ")
print(len(seleccionArgentina))

# Agregamos jugadores
seleccionArgentina[9]= {"Nombre": "Gonzalo Higuaín", "Edad": 34, "Altura": 1.84, "Precio": "25 Millones", "Posición": "Delantero"}
seleccionArgentina[5]= {"Nombre": "Leandro Paredes", "Edad": 27, "Altura": 1.80, "Precio": "20 Millones", "Posición": "Centrocampista"}
seleccionArgentina[17]= {"Nombre": "Nicolás Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "15 Millones", "Posición": "Defensor"}
seleccionArgentina[21] = {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "40 Millones", "Posición": "Delantero"}

for llave, valor in seleccionArgentina.items():
    print(llave,valor)
print("Tenemos cargados en el diccionario una cantidad de jugadores: ", end=" ")
print(len(seleccionArgentina))

# Pilas isando listas
pila = [1, 2, 3]

# Agregamos elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop()  # Quita el ultimo elemento y lo guarda en la vairable
print(f"Sacamos el elemtno: {elementoBorrado}")
print(f"La pila ahora queda asi: {pila}")