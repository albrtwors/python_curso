# EL encapsulamiento no es mas que definir los permisos de acceso de las propiedades como los metodos

class Lapiz:
    # privadas: que nada mas pueden ser accesibles desde el mismo objeto
    _dibujo='Perro'
    def dibujar(self):
        print(f'dibujaste un {self._dibujo}')


    #propiedad privada
    def _dañarse(self):
        print('se dañó el lápiz')
    
    # GETTER: Funcion que te va retornar el valor o la funcion privada que desees
    def get_dibujo(self):
        return self._dibujo
    def get_dañarse(self):
        self._dañarse()

    # SETTER: Asignar valores | metodo que asigna valores a propiedades privadas
    def set_dibujo(self, dibujo):
        self._dibujo=dibujo
    

    

lapiz=Lapiz()
lapiz.set_dibujo('Gato')
print(lapiz.get_dibujo())

