from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from core.models import Contato_professor
# Create your views here.
def index(request):
    return render(request,"index.html")

def curso(request):
    return render(request, "curso.html")

def noticia(request):
    return render(request, "noticia.html")

def detalhe(request):
    return render(request, "detalhe.html")

def disciplina(request):
    return render(request, "disciplina.html")

def formulario_login(request):
    return render(request, "formulario_login.html")

def formulario_esqueciasenha(request):
    return render(request, "formulario_esqueciasenha.html")

def formulario_contato(request):
    return render(request, "formulario_contato.html")

def formulario_disciplina(request):
    return render(request, "formulario_disciplina.html")

def formulario_cadastro(request):
    return render(request, "formulario_cadastro.html")
    
def pagina_aluno(request):
    return render(request, "pagina_aluno.html")


def exerciciosetrabalhos_aluno(request):
    return render(request, "exerciciosetrabalhos_aluno.html")


def formulario_cancelamento(request):
    return render(request, "formulario_cancelamento.html")

def formulario_enviarmsg(request):
    return render(request, "formulario_enviarmsg.html")

def menualuno(request):
    return render(request, "menualuno.html")

def notas(request):
    return render(request, "notas.html")

def resumodasentregaspendentes(request):
    return render(request, "resumodasentregaspendentes.html")

def carreira(request):
    return render(request, "carreira.html")  

def horario(request):
    return render(request, "horario.html")  

def cancelamentodematricula(request):
    return render(request, "cancelamentodematricula.html") 

def notas(request):
    return render(request, "notas.html")    

def pagina_professor(request):
    return render(request, "pagina_professor.html")  

def resumodasentregasrecebidas(request):
    return render(request, "resumodasentregasrecebidas.html") 

def trabalhoeexercicio(request):
    return render(request, "trabalhoeexercicio.html")  
 
#============CARLOS RIAN COMENTOI AS LINHAS ABAIXO===============#
#def contatoprofessores(request):
    #return render(request, "contatoprofessores.html")    
#=============CARLOS RIAN COMENTOI AS LINHAS ACIMA===============#
#
# 
# 
# 
#============CARLOS RIAN EDITOU AS LINHAS ABAIXO===============#
def contato_professor(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'contatoprofessores.html',
        context_instance = RequestContext(request,
        {
            'title':'Contato Professor',
            'contato_professor': Contato_professor.objects.all(),
            'year':datetime.now().year,
        })
    ) 
def formulario_professor(request):
    return render(request, "formulario_professor.html")  
#=============CARLOS RIAN EDITOU AS LINHAS ACIMA===============#
