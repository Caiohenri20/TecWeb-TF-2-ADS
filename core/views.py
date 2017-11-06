from django.shortcuts import render

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
