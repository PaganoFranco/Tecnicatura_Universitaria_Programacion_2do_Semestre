class Persona2:
    def __init__(self, nombre, apellido, edad): # Esta encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self.nombre} {self.apellido} {self.edad}")
    @property # decorador
    def nombre(self): # Metodo getter
        print("Estamos utilizando el metodo get")
        return self._nombre
    @nombre.setter
    def nombre(self, nombre): # Metodo setter
        print("Estamos utilizando el metodo set")
        self._nombre = nombre

    @property  # decorador
    def apellido(self):  # Metodo getter
        # print("Estamos utilizando el metodo get")
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Metodo setter
        #print("Estamos utilizando el metodo set")
        self._apellido = apellido

    @property  # decorador
    def edad(self):  # Metodo getter
        # print("Estamos utilizando el metodo get")
        return self._edad

    """
    @edad.setter
    def edad(self, edad):  # Metodo setter
        # print("Estamos utilizando el metodo set")
        self._edad = edad
    """

persona1 = Persona2("Franco", "Pagano", 26)
print(persona1.nombre) # de esta forma llamamos al metodo getter
persona1.nombre = "Juan Pablo"
print(persona1.nombre)
print(persona1.mostrar_detalles())
# persona1._edad = 40 ESTO NO SE HACE
# Atributos read-only seria la edad porque no tiene el metodo set
print(persona1.edad)
