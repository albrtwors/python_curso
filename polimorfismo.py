# Reescribir los metodos de la clase padre en una herencia 

class Animal:
    def caminar(self):
        print('Estas caminando')

class Human(Animal):
    def caminar(self):
        print('Estas caminando a 2 patas')

jeff=Human()
jeff.caminar()
