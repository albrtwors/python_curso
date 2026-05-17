python3 -m django startproject folder project-folder 
correrlo
python3 manage.py runserver


# crear una app | que es un app en django?
##### como un modulo de la aplicacion
# Ejemplo en steam
##### app-library, vistas para ver todos los juegos, detalle del juego 
##### app-community, workshop ,market, discussions
##### app-user, friends, config, badges, inventory
##### app-store, vistas para ver los juegos a comprar, wishlist, point shop 

##### app-polls, preguntas y sus respectivas choices
# MODULO POLLS
python3 manage.py startapp poll
## crear una vista 
#### urls.py es el encargado de la ruta
#### views.py es el encargado de las funciones de vistas ( o controladores) modelo vista plantilla

## MODELOS
#### Modelo va a ser la entidad encargada de manipular la base de datos
##### por cada tabla vamos a tener un modelo, Modelo Question tiene una o mas choices, # Modelo Choice pertenece a una question

# migrations | laravel las migrations eran como un shortcut para crear tablas de base de datos
 python3 manage.py migrate
#### una vez puestas las settings, y creadas las entidades o los modelos usamos este comando para crear las migraciones
python3 manage.py makemigrations poll (el mismo nombre de la app con los modelos)
python3 manage.py migrate

python manage.py createsuperuser # crear usuario admin

#### para incorporar los registros de modelos al panel de admin simplemente en el admin.py de nuestra app incluimos lo siguiente:

from django.contrib import admin
from .models import Question

admin.site.register(Question)
