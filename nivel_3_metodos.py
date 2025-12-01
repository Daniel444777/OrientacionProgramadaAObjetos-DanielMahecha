# Clase Coche que incluye métodos
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False # Atributo de estado

    # Método para encender el coche (Comportamiento)
    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El {self.marca} {self.modelo} ha sido encendido. ¡Listo para rodar!")
        else:
            print("El coche ya estaba encendido.")

    # Método para apagar el coche (Comportamiento)
    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"El {self.marca} {self.modelo} ha sido apagado.")
        else:
            print("El coche ya estaba apagado.")

    # Método para obtener la descripción (Comportamiento)
    def describir(self):
        estado = "encendido" if self.encendido else "apagado"
        return f"Coche {self.marca} {self.modelo}, color {self.color}, actualmente {estado}."

# --- Usando la Clase y sus Métodos ---

coche_deportivo = Coche("Ferrari", "SF90", "Amarillo")

# 1. Descripción inicial
print(coche_deportivo.describir())

# 2. Ejecutar un método (Encender)
coche_deportivo.encender()

# 3. Intentar encender de nuevo
coche_deportivo.encender()

# 4. Descripción después de encender
print(coche_deportivo.describir())

# 5. Ejecutar otro método (Apagar)
coche_deportivo.apagar()
print(coche_deportivo.describir())