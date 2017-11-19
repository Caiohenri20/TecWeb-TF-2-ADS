
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


urlpatterns = patterns('',

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
    url(r'^pagina_professor', pagina_professor),
    url(r'^formulario_professor', formulario_professor),
    url(r'^notas', notas),    
    url(r'^exerciciosetrabalhos_aluno', exerciciosetrabalhos_aluno),   

    url(r'^listar_aluno', 'core.views.listar_aluno', name='listar_aluno'),
    url(r'^novo_aluno', 'core.views.novo_aluno', name='novo_aluno'),
    url(r'^editar_aluno/(?P<pk>\d+)$', 'core.views.editar_aluno', name='editar_aluno'),
    url(r'^apagar_aluno/(?P<pk>\d+)$', 'core.views.apagar_aluno', name='apagar_aluno'),

    url(r'^listar_curso', 'core.views.listar_curso', name='listar_curso'),
    url(r'^novo_curso', 'core.views.novo_curso', name='novo_curso'),
    url(r'^editar_curso/(?P<pk>\d+)$', 'core.views.editar_curso', name='editar_curso'),
    url(r'^apagar_curso/(?P<pk>\d+)$', 'core.views.apagar_curso', name='apagar_curso'),

    url(r'^listar_cursturma', 'core.views.listar_cursturma', name='listar_cursturma'),
    url(r'^novo_cursturma', 'core.views.novo_cursturma', name='novo_cursturma'),
    url(r'^editar_cursturma/(?P<pk>\d+)$', 'core.views.editar_cursturma', name='editar_cursturma'),
    url(r'^apagar_cursturma/(?P<pk>\d+)$', 'core.views.apagar_cursturma', name='apagar_cursturma'),

    url(r'^listar_disciplina', 'core.views.listar_disciplina', name='listar_disciplina'),
    url(r'^novo_disciplina', 'core.views.novo_disciplina', name='novo_disciplina'),
    url(r'^editar_disciplina/(?P<pk>\d+)$', 'core.views.editar_disciplina', name='editar_disciplina'),
    url(r'^apagar_disciplina/(?P<pk>\d+)$', 'core.views.apagar_disciplina', name='apagar_disciplina'),

    url(r'^listar_disciplinofertada', 'core.views.listar_disciplinofertada', name='listar_disciplinofertada'),
    url(r'^novo_disciplinofertada', 'core.views.novo_disciplinofertada', name='novo_disciplinofertada'),
    url(r'^editar_disciplinofertada/(?P<pk>\d+)$', 'core.views.editar_disciplinofertada', name='editar_disciplinofertada'),
    url(r'^apagar_disciplinofertada/(?P<pk>\d+)$', 'core.views.apagar_disciplinofertada', name='apagar_disciplinofertada'),

    url(r'^listar_grade', 'core.views.listar_grade', name='listar_grade'),
    url(r'^novo_grade', 'core.views.novo_grade', name='novo_grade'),
    url(r'^editar_grade/(?P<pk>\d+)$', 'core.views.editar_disciplina', name='editar_grade'),
    url(r'^apagar_grade/(?P<pk>\d+)$', 'core.views.apagar_grade', name='apagar_grade'),

    url(r'^listar_matricula', 'core.views.listar_matricula', name='listar_matricula'),
    url(r'^novo_matricula', 'core.views.novo_matricula', name='novo_matricula'),
    url(r'^editar_matricula/(?P<pk>\d+)$', 'core.views.editar_matricula', name='editar_matricula'),
    url(r'^apagar_matricula/(?P<pk>\d+)$', 'core.views.apagar_matricula', name='apagar_matricula'),

    url(r'^listar_periodo', 'core.views.listar_periodo', name='listar_periodo'),
    url(r'^novo_periodo', 'core.views.novo_periodo', name='novo_periodo'),
    url(r'^editar_periodo/(?P<pk>\d+)$', 'core.views.editar_periodo', name='editar_periodo'),
    url(r'^apagar_periodo/(?P<pk>\d+)$', 'core.views.apagar_periodo', name='apagar_periodo'),

    url(r'^listar_perioddisciplina', 'core.views.listar_perioddisciplina', name='listar_perioddisciplina'),
    url(r'^novo_perioddisciplina', 'core.views.novo_perioddisciplina', name='novo_perioddisciplina'),
    url(r'^editar_perioddisciplina/(?P<pk>\d+)$', 'core.views.editar_perioddisciplina', name='editar_perioddisciplina'),
    url(r'^apagar_perioddisciplina/(?P<pk>\d+)$', 'core.views.apagar_perioddisciplina', name='apagar_perioddisciplina'),

    url(r'^listar_professor', 'core.views.listar_professor', name='listar_professor'),
    url(r'^novo_professor', 'core.views.novo_professor', name='novo_professor'),
    url(r'^editar_professor/(?P<pk>\d+)$', 'core.views.editar_professor', name='editar_professor'),
    url(r'^apagar_professor/(?P<pk>\d+)$', 'core.views.apagar_professor', name='apagar_professor'),

    url(r'^listar_turma', 'core.views.listar_turma', name='listar_turma'),
    url(r'^novo_turma', 'core.views.novo_turma', name='novo_turma'),
    url(r'^editar_turma/(?P<pk>\d+)$', 'core.views.editar_turma', name='editar_turma'),
    url(r'^apagar_turma/(?P<pk>\d+)$', 'core.views.apagar_turma', name='apagar_turma'),

    url(r'^listar_questao', 'core.views.listar_questao', name='listar_questao'),
    url(r'^novo_questao', 'core.views.novo_questao', name='novo_questao'),
    url(r'^editar_questao/(?P<pk>\d+)$', 'core.views.editar_questao', name='editar_questao'),
    url(r'^apagar_questao/(?P<pk>\d+)$', 'core.views.apagar_questao', name='apagar_questao'),

    url(r'^listar_resposta', 'core.views.listar_resposta', name='listar_resposta'),
    url(r'^novo_resposta', 'core.views.novo_resposta', name='novo_resposta'),
    url(r'^editar_resposta/(?P<pk>\d+)$', 'core.views.editar_resposta', name='editar_resposta'),
    url(r'^apagar_resposta/(?P<pk>\d+)$', 'core.views.apagar_resposta', name='apagar_resposta'),

    url(r'^listar_arquivresposta', 'core.views.listar_arquivresposta', name='listar_arquivresposta'),
    url(r'^novo_arquivresposta', 'core.views.novo_arquivresposta', name='novo_arquivresposta'),
    url(r'^editar_arquivresposta/(?P<pk>\d+)$', 'core.views.editar_arquivresposta', name='editar_arquivresposta'),
    url(r'^apagar_arquivresposta/(?P<pk>\d+)$', 'core.views.apagar_arquivresposta', name='apagar_arquivresposta'),

    url(r'^listar_arquivquestao', 'core.views.listar_arquivquestao', name='listar_arquivquestao'),
    url(r'^novo_arquivquestao', 'core.views.novo_arquivquestao', name='novo_arquivquestao'),
    url(r'^editar_arquivquestao/(?P<pk>\d+)$', 'core.views.editar_arquivquestao', name='editar_arquivquestao'),
    url(r'^apagar_arquivquestao/(?P<pk>\d+)$', 'core.views.apagar_arquivquestao', name='apagar_arquivquestao'),

)
