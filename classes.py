# OOP Paradigma | Estilo
# polimorfismo | abstraccion | herencia | encapsulamiento
# atributos y metodos 
# Clase (plantilla) | objeto instancia o la creacion

class Car:
    color='Rojo'
    marca='Chevrolet'

    def arrancar(self):
        print('Haz arrancado')

car1 = Car()
print(car1.color)
car1.arrancar()

class Bed:
    color='Marron'
    tipo='Matrimonial'
    def organizar(self):
        print('Organizaste la cama')

bed1 = Bed()
print(bed1.tipo)
bed1.organizar()