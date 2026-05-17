#urlpatterns | encargado de definir las rutas y sus respectivas vistas
from django.urls import path
from . import views
#va a ser la encargada de enrutar, es decir relacionar una ruta web /polls, con una funcion de views.py
urlpatterns=[
    path('', views.index, name="index"),
    path('overview/', views.overview, name="overview") 
]

# registrar estas rutas de urls.py en la aplicacion mysite