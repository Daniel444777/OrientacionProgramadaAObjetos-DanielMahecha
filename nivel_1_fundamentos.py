# Definición de la Clase (el "molde")
# Representa un Estudiante genérico.
class Estudiante:
    # Atributo de Clase: Es común a todos los estudiantes
    tipo_persona = "Humano"

# --- Creación de Objetos (Instancias) ---

# 1. Crear el objeto 'estudiante_1'
estudiante_1 = Estudiante()

# 2. Asignar atributos específicos al objeto 'estudiante_1'
estudiante_1.nombre = "Laura Vásquez"
estudiante_1.edad = 21
estudiante_1.promedio = 4.5

# 3. Crear el objeto 'estudiante_2'
estudiante_2 = Estudiante()
estudiante_2.nombre = "Carlos Mena"
estudiante_2.edad = 19
estudiante_2.promedio = 3.8

# --- Acceder a los Atributos ---

print("--- Estudiante 1 ---")
print(f"Nombre: {estudiante_1.nombre}")
print(f"Edad: {estudiante_1.edad}")
print(f"Promedio: {estudiante_1.promedio}")
print(f"Tipo: {estudiante_1.tipo_persona}") # Accede al atributo de clase

print("\n--- Estudiante 2 ---")
print(f"Nombre: {estudiante_2.nombre}")
print(f"Promedio: {estudiante_2.promedio}")
print(f"Tipo: {estudiante_2.tipo_persona}")