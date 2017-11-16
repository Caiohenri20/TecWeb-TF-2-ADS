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

class UsuarioManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, ra, password, **extra_fields):
        if not ra:
            raise ValueError('RA precisa ser preenchido')
        user = self.model(ra=ra, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, ra, password=None, **extra_fields):
        return self._create_user(ra, password, **extra_fields)

    def create_superuser(self, ra, password, **extra_fields):
        return self._create_user(ra, password, **extra_fields)


class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=50)
    ra= models.IntegerField( unique=True)
    password = models.CharField(max_length=150)
    perfil = models.CharField(max_length=1, default='c')
    ativo = models.BooleanField(default=True)


    USERNAME_FIELD = 'ra'
    REQUIRED_FIELDS = ['nome']

    objects = UsuarioManager()

    
    def is_staff(self):
        return self.perfil == 'c'


#=============CAIO EDITOU AS LINHAS ACIMA===============#


