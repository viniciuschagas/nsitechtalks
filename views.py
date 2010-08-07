from django.shortcuts import render_to_response
from django.template import RequestContext
from techtalks.models import Edicao

def index(request):
    edicao_em_destaque = Edicao.objects.filter(em_destaque=True)[0]
    return render_to_response(
        'index.html',
        {'edicao_em_destaque':edicao_em_destaque},
        context_instance=RequestContext(request)
    )