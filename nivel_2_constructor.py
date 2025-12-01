# Clase Coche con Constructor __init__
class Coche:
    # El método __init__ es el constructor. Se llama automáticamente al crear el objeto.
    # Los atributos se inicializan usando 'self'.
    def __init__(self, marca, modelo, color):
        self.marca = marca      # Atributo
        self.modelo = modelo    # Atributo
        self.color = color      # Atributo
        self.encendido = False  # Estado inicial

# --- Creación de Objetos con Parámetros ---

# Al crear los objetos, pasamos los valores directamente
mi_coche = Coche("Toyota", "Corolla", "Rojo")
otro_coche = Coche("Renault", "Sandero", "Blanco")

# --- Verificar los Atributos ---

print("--- Mi Coche ---")
print(f"Marca: {mi_coche.marca}")
print(f"Modelo: {mi_coche.modelo}")
print(f"Encendido: {mi_coche.encendido}") # Estado inicial: False

print("\n--- Otro Coche ---")
print(f"Marca: {otro_coche.marca}")
print(f"Color: {otro_coche.color}")