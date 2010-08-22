# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Edicao, Palestrante

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