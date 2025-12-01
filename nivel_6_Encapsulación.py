class EmpleadoEncapsulado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario # Atributo privado

    # Método Público (Getter) para leer el salario
    def obtener_salario(self):
        return self.__salario
    
    # Método Público (Setter) para modificar el salario con una validación
    def establecer_salario(self, nuevo_salario):
        if nuevo_salario >= 0:
            self.__salario = nuevo_salario
            print("Salario actualizado.")
        else:
            print("Error: El salario no puede ser negativo.")

# Uso
e = EmpleadoEncapsulado("Juan", 1000)
print(e.obtener_salario()) # Acceso correcto a través del método (Getter)
# print(e.__salario) # Esto generaría un error de acceso
e.establecer_salario(1200) # Modificación controlada (Setter)