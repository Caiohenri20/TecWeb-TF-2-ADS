from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here. 
#
#============CARLOS RIAN EDITOU AS LINHAS ABAIXO===============#
class Contato_professor(models.Model):
    professor = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)
    aviso = models.CharField(max_length=400)
#=============CARLOS RIAN EDITOU AS LINHAS ACIMA===============# 

#============CAIO EDITOU AS LINHAS ABAIXO===============#


class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=50)
    ra= models.IntegerField( unique=True)
    password = models.CharField(max_length=150)
    perfil = models.CharField(max_length=1, default='c')
    ativo = models.BooleanField(default=True)


    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome']


#=============CAIO EDITOU AS LINHAS ACIMA===============# 



