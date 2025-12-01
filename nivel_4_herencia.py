# --- Superclase (Clase Padre) ---
class Empleado:
    # Constructor que inicializa atributos comunes
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    # Método común a todos los empleados
    def describir(self):
        return f"Nombre: {self.nombre}, Salario: ${self.salario:,.2f}"

# --- Subclase (Clase Hija) ---
# Programador hereda de Empleado
class Programador(Empleado):
    # El constructor de la hija llama al constructor del padre (super)
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje # Nuevo atributo específico

    # Método específico de la subclase
    def programar(self):
        print(f"{self.nombre} está programando en {self.lenguaje}.")
        
    # Podemos sobrescribir (override) el método describir
    def describir(self):
        # Usamos el método describir del padre y agregamos información
        info_padre = super().describir()
        return f"{info_padre}, Lenguaje Principal: {self.lenguaje}."

# --- Usando las Clases ---
empleado_base = Empleado("Ana Pérez", 50000)
programador_junior = Programador("Luis Gómez", 65000, "Python")

print("--- Empleado Base ---")
print(empleado_base.describir())

print("\n--- Programador ---")
print(programador_junior.describir())
programador_junior.programar()