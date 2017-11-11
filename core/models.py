from django.db import models

# Create your models here. 
# 
# 
#============CARLOS RIAN EDITOU AS LINHAS ABAIXO===============#
class Contato_professor(models.Model):
    professor = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=100)
    aviso = models.CharField(max_length=400)
#=============CARLOS RIAN EDITOU AS LINHAS ACIMA===============# 
