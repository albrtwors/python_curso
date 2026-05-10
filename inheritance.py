# Herencia 

# RPG
class Personaje:
    def __init__(self, nombre):
        self.nombre=nombre

    def saludar(self):
        print(self.nombre)

# Clase hija 
class Caballero(Personaje):
    def __init__(self, nombre, espada, armadura):
        self.espada = espada 
        self.armadura = armadura
        # SIEMPRE VA A ESTAR PENDIENTE INICIALIZAR LOS DATOS DEL PADRE
        super().__init__(nombre)

class Militar(Caballero):
    def __init__(self, nombre, espada, armadura):    
        super().__init__(nombre, espada, armadura)
    

caballero1 = Caballero('Luke Skywalker', 'Lightsaber', 'Nada')
caballero1.saludar()
print(caballero1.espada)