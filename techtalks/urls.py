from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$','techtalks.views.index'),
    (r'^palestrante/(?P<palestrante_id>\d+)/$','techtalks.views.palestrante'),
    (r'^anteriores/$','techtalks.views.anteriores'),
    (r'^arquivos/$','techtalks.views.arquivos'),
    (r'^fotos_edicao/(?P<edicao_id>\d+)/$','techtalks.views.fotos_edicao'),
    (r'^videos_edicao/(?P<edicao_id>\d+)/$','techtalks.views.videos_edicao'),
    (r'^detalhes_edicao/(?P<edicao_id>\d+)/$','techtalks.views.detalhes_edicao'),
    (r'^detalhes_palestra/(?P<palestra_id>\d+)/$','techtalks.views.detalhes_palestra'),
    (r'^contato/$', 'techtalks.views.contato'),
    (r'^sucesso_contato/$','django.views.generic.simple.direct_to_template',
        {'template':'sucesso_contato.html'}),
    (r'^equipe/$','techtalks.views.equipe'),
    (r'^filtrar_por_tag/(?P<tag>\w+)/$','techtalks.views.buscar_palestrar_por_tag'),
    
)

