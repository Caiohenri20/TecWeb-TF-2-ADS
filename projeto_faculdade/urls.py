"""lmsimpacta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from datetime import datetime
from django.conf.urls import url    
from django.contrib import admin

from core.views import index
from core.views import curso
from core.views import noticia
from core.views import detalhe
from core.views import disciplina
from core.views import formulario_login
from core.views import formulario_esqueciasenha
from core.views import formulario_contato
from core.views import formulario_disciplina
from core.views import formulario_cadastro
from core.views import pagina_aluno
from core.views import carreira
from core.views import horario 
from core.views import cancelamentodematricula  
from core.views import notas  
from core.views import contato_professor,pagina_professor
from core.views import exerciciosetrabalhos_aluno, formulario_professor
from core.views import resumodasentregasrecebidas 
from core.views import trabalhoeexercicio
from core.views import formulario_vestibular
from core.views import formulario_smartclassprof
from core.views import formulario_smartclassaluno
from core.views import entregatrabalho_aluno


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^curso', curso),
    url(r'^noticia', noticia),
    url(r'^detalhe', detalhe),
    url(r'^disciplina', disciplina),
    url(r'^formulario_login', formulario_login),
    url(r'^formulario_esqueciasenha', formulario_esqueciasenha),
    url(r'^formulario_contato', formulario_contato),
    url(r'^formulario_disciplina', formulario_disciplina),
    url(r'^formulario_cadastro', formulario_cadastro),
    url(r'^pagina_aluno', pagina_aluno),
    url(r'^carreira', carreira),
    url(r'^horario', horario),
    url(r'^cancelamentodematricula', cancelamentodematricula),  
    url(r'^contato_professor', contato_professor),
    url(r'^pagina_professor', pagina_professor),
    url(r'^formulario_professor', formulario_professor),
    url(r'^notas', notas),    
    url(r'^exerciciosetrabalhos_aluno', exerciciosetrabalhos_aluno),    
    url(r'^resumodasentregasrecebidas', resumodasentregasrecebidas), 
    url(r'^trabalhoeexercicio', trabalhoeexercicio), 
    url(r'^formulario_vestibular', formulario_vestibular), 
    url(r'^formulario_smartclassprof', formulario_smartclassprof),
    url(r'^formulario_smartclassaluno', formulario_smartclassaluno),
    url(r'^entregatrabalho_aluno', entregatrabalho_aluno),
]
