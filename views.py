from django.shortcuts import render_to_response
from django.template import RequestContext
from techtalks.models import Edicao

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