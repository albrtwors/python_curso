#static: que no necesitas instanciar el objeto
class Math:

    @staticmethod #metodo estatico
    def sumar(a,b):
        return a+b

print(Math.sumar(1,2))