MVC es una arquitectura, no es un patron de diseño.
Modelo: para manipular entidades de la base de datos. Es un componente encargado de comunicarse con la DB (laravel, django).

Modelo Venta. Modelo Envio. Modelo Inventario.  #lenguaje mas sencillo

Vista: frontend, todo lo que el usuario visualiza. php

Controlador: intermediario, componente encargado de conectar las vistas a los modelos. Orquestador,

MVC VANILLA
class ProductoModelo:

    def crear:
        INSERT INTO TABLE (1,2,3) VALUES (1,2,3)

    def eliminar:

