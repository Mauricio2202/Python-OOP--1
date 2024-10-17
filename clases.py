# Aquí definimos la clase persona
class Persona:
    # Acá iniciamos el método constructor con sus atributos
    def __init__(self, nombre, edad, nacionalidad, empleo, salario):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.empleo = empleo
        self._salario = salario
        
    # Método para mostrar datos
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Nacionalidad: {self.nacionalidad}")

# Herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, empleo, salario, grado):
        # Solo heredamos lo que tiene persona, y agregamos grado
        super().__init__(nombre, edad, nacionalidad, empleo, salario)
        self.grado = grado

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Salario: {self._salario}")

# Agregamos los atributos para la clase PERSONA
alisson = Persona("Alisson", 18, "Colombiana", "Programadora", 25000)
# Agregamos los atributos para la clase ESTUDIANTE
jeilin = Estudiante("Jeilin", 20, "Colombiana", "Programador", 25000, "Octavo")

# MOSTRAMOS DATOS
alisson.mostrar_datos()
print("---------------------------------------------------")
jeilin.mostrar_datos()

# FIRMES Y DIGNOS... Att. OmegaDev