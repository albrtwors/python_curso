# constructor es un metodo de la clase, que te va a permitir inicializarla con x valores
class Bed:
    def __init__(self, color, tipo): # constructor
        self.color=color
        self.tipo=tipo

    def organizar(self):
        print(f"Organizaste la cama de color {self.color}")

bed1=Bed('Rojo', 'Individual')


class PS3:
    def __init__(self, color, modelo, juegos, puertos):
        self.color=color
        self.modelo=modelo
        self.juegos=juegos
        self.puertos=puertos

    def jugar(self):
        print(f"Ahora estás jugando en tu PS3 {self.modelo} de color {self.color}")

listado_juegos = {
    'Resident Evil 4': 'Survival Horror',
    'Sonic Unleashed': 'Plataformas',
    'Call of Duty': 'Shooter'
}

ps3_1=PS3('Blanca','Super Slim', listado_juegos, 7)
print(ps3_1.juegos)