from django.db import models

# Create your models here.
# Choice Question
#herencia
# MODELO, ES MANIPULAR DATOS DE LA BD, CONTROLADOR
class Question(models.Model):
    #propiedades | campos de la base de datos
    # id (pk) ya viene por defecto en django
    question_text=models.CharField(max_length=200)
    question_difficulty=models.IntegerField()

class Choice(models.Model):
    choice_text=models.CharField(max_length=200)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)


# ORM , OBJECT RELATIONAL MAPPER
