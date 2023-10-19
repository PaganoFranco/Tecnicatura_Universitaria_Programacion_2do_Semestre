class Persona:  # Creamos una clase
    def __init__(self):  # Se lo llama metodo INIT DUNDER
        self.nombre = "Franco"
        self.apellido = "Pagano"
        self.edad = 26

persona1 = Persona()  # Constructor
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)