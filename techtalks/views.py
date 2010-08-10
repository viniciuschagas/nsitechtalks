# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Edicao, Palestrante

def index(request):
    try:
        edicao_em_destaque = Edicao.objects.filter(status='proxima')[0]
    except IndexError:
        edicao_em_destaque = None
    return render_to_response(
        'index.html',
        {'edicao_em_destaque':edicao_em_destaque},
        context_instance=RequestContext(request)
    )
    
def palestrante(request,palestrante_id):
    palestrante = Palestrante.objects.get(id=palestrante_id)
    return render_to_response(
        'detalhes_palestrante.html',
        {'palestrante':palestrante},
        context_instance=RequestContext(request)
    )