# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from models import Edicao, Palestrante, PalavraChave, Palestra
from forms import FormularioDeContato

def index(request):
    try:
        edicao = Edicao.objects.filter(status='proxima')[0]
    except IndexError:
        edicao = None
    return render_to_response(
        'index.html',
        {'edicao':edicao},
        context_instance=RequestContext(request)
    )
    
def palestrante(request,palestrante_id):
    palestrante = Palestrante.objects.get(id=palestrante_id)
    return render_to_response(
        'detalhes_palestrante.html',
        {'palestrante':palestrante},
        context_instance=RequestContext(request)
    )

def anteriores(request):
    anteriores = Edicao.objects.filter(status='realizada').order_by("id")
    return render_to_response(
        'anteriores.html',
        {'anteriores':anteriores},
        context_instance=RequestContext(request)
    )

def detalhes_edicao(request, edicao_id):
    edicao = Edicao.objects.get(id=edicao_id)
    return render_to_response(
        'detalhes_edicao.html',
        {'edicao':edicao},
        context_instance=RequestContext(request)
    )
    
def detalhes_palestra(request, palestra_id):
    palestra = Palestra.objects.get(id=palestra_id)
    return render_to_response(
        'detalhes_palestra.html',
        {'palestra':palestra},
        context_instance=RequestContext(request)
    )
    
def arquivos(request):
    edicoes_realizadas = Edicao.objects.filter(status='realizada').order_by("id")
    return render_to_response(
        'arquivos.html',
        {'edicoes_realizadas':edicoes_realizadas},
        context_instance=RequestContext(request)
    )
    
def fotos_edicao(request,edicao_id):
    edicao = Edicao.objects.get(id=edicao_id)
    fotos = edicao.listar_fotos()
    return render_to_response(
        'fotos_edicao.html',
        {'fotos':fotos,'edicao':edicao},
        context_instance=RequestContext(request)
    )

def videos_edicao(request,edicao_id):
    pass
    
def contato(request):
    if request.method  == 'POST':
        formulario_contato = FormularioDeContato(request.POST)
        if formulario_contato.is_valid():
            nome = request.POST.get('nome')
            email = request.POST.get('email')
            assunto = request.POST.get('assunto')
            mensagem = request.POST.get('mensagem')
            send_mail(assunto,mensagem,email,['email@server.com'],fail_silently=False)
            return HttpResponseRedirect('/sucesso_contato/')
        else:
            return render_to_response(
                'contato.html',
                {'form':formulario_contato},
                context_instance=RequestContext(request)
            )
    else:
        form = FormularioDeContato()
        return render_to_response(
            'contato.html',
            {'form':form},
            context_instance=RequestContext(request)
        )
        
def equipe(request):
    return render_to_response(
        'equipe.html',
        context_instance=RequestContext(request)
    )
    
def buscar_palestrar_por_tag(request,tag):
    palavra_chave = PalavraChave.objects.get(titulo=tag)
    palestras = Palestra.objects.filter(palavras_chave=palavra_chave)
    return render_to_response(
        'buscar_palestras_por_tag.html',
        {'palestras':palestras,'tag':tag},
        context_instance=RequestContext(request)
    )