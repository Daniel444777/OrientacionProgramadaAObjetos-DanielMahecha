# --- Clases con el mismo método (hacer_sonido) ---

class Perro:
    def hacer_sonido(self):
        return "Guau, guau!"

class Gato:
    def hacer_sonido(self):
        return "Miau, miau..."

class Vaca:
    def hacer_sonido(self):
        return "Muuu!"

# --- Función Polimórfica ---
# Esta función no necesita saber qué tipo de objeto es, solo que tenga el método 'hacer_sonido'.
def escuchar_animal(animal):
    print(f"El animal dice: {animal.hacer_sonido()}")

# --- Usando el Polimorfismo ---

perro_obj = Perro()
gato_obj = Gato()
vaca_obj = Vaca()

# La misma función 'escuchar_animal' se comporta diferente
# dependiendo del objeto que le pasamos.
escuchar_animal(perro_obj)
escuchar_animal(gato_obj)
escuchar_animal(vaca_obj)