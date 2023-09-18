"""
Ejercicio 3: Agregar personajes a una lista
Escriba un programa donde cree una lista con los siguientes personajes
del señor de los anillos
Nombre: Aragon
Clase: Gerrero
Raza: Dunadan del norte

Nombre Gandalf
Clase: Mago
Raza: Islar

Nombre: Legolas
Clase: Arquero
Raza: Elfo Sindar
"""

personajes = [] # Creamos una lista vacia
# Creamos diccionarios
P = {"Nombre": "Aragon", "Clase": "Gerrero", "Raza" : "Dunadan del Norte"}
personajes.append(P)
P = {"Nombre": "Gandalf", "Clase": "Mago", "Raza" : "Islar"}
personajes.append(P)
P = {"Nombre": "Legolas", "Clase": "Arquero", "Raza" : "Elfo Sindar"}
personajes.append(P)
print(personajes)