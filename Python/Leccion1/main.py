# lista = Elemento1, Elemento2, Elemento3, Elemento4
"""
Al crear una lista, los elementos toman posiciones como elementos de un conjunto.
"""
nombres = ["Elemento1", "Elemento2", "Elemento3", "Elemento4"]
print(nombres)
"""
Para recorrer del primer elemento al ultimo:
"""
print(nombres[0]) #Podemos visualizar un elemento en espesifico de la lista
print(nombres[1])
print(nombres[2])
print(nombres[-1]) #podemos visualizar el ultimo elemento, sin saber cual es
"""
Para recorrer del ultimo  elemento al primero:
"""
print(nombres[-1])
print(nombres[-2])
print(nombres[-3])

#-----------------------------------------------------------------------
nombres = ["Elemento1", "Elemento2", "Elemento3", "Elemento4"]
print(nombres)
print(nombres[0:2]) #Podemos visualizar los elementos dentro del rango nombres[0] y nombres[1]
print(nombres[ :3]) #Podemos visualizar desde el primer elemento hasta el nombres[2]
print(nombres[1: ]) #Podemos visualizar desde el nombres[1] hasta el ultimo

#Modificar un valor dentro de la lista
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
print(nombres)

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

# Eliminar la lista
del nombres
print(nombres) stat