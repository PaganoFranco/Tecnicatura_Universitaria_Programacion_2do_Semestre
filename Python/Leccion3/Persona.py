class Persona:  # Creamos una clase
    def __init__(self, nombre, apellido, edad, *args, **kwargs):  # Se lo llama metodo INIT DUNDER
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalles(self): # self es igual a this en java
        print(f"La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}")


persona1 = Persona("Franco", "Pagano", 26)  # Necesitamos enviar argumentos
"""
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)   
"""
# Tarea hacer un print con interpolacion:
print(f"El objeto de la clase persona1: {persona1.nombre} {persona1.apellido} su edad es {persona1.edad}")

persona2 = Persona("Julieta", "Quiroga", 27)
print(f"El objeto de la clase persona2: {persona2.nombre} {persona2.apellido} su edad es {persona2.edad}")

persona1.nombre = "Viviana"
persona1.apellido = "Pantaley"
persona1.edad = 62
print(f"El objeto de la clase persona1: {persona1.nombre} {persona1.apellido} su edad es {persona1.edad}")

# Los atributos son: CARACTERISTICAS
# Los metodos son: el comportameitno que van a tener los objetos (acciones)
persona1.mostrar_detalles() # la refencia en este caso se pasa de manerea automatica
persona2.mostrar_detalles()

# Persona.mostrar_detalles(persona1) #Debemos pasarle una referencia para el self o dara error
persona1.telefono = "2604694746"
print(f"este es el telefono de {persona1.nombre}: {persona1.telefono} ")

# print(persona2.telefono) " El objeto persona 2 no tiene este atributo
persona3 = Persona("Franco", "Pagano", 26, "Tefelono", "2604694746", "Calle Av Pagano", 857, "Manzana", 4, "Casa", 18, Altura = 1.83, Perso = 110, CFavorito = "Rojo", Modelo = 2023)
persona3.mostrar_detalles()