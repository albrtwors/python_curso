class Vaso:
    def __init__(self):
        self.color="Azul"
        self.tamaño="Pequeño"
        self.material="Vidrio"

    def llenar(self):
        print("Has llenado el vaso")

    def obtener_descripcion(self):
        return f"El vaso es de color {self.color}, tamaño {self.tamaño} y material {self.material}"

vaso = Vaso()
print(vaso.obtener_descripcion())
vaso.llenar()