from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$','techtalks.views.index'),
    (r'^palestrante/(?P<palestrante_id>\d+)/$','techtalks.views.palestrante'),
    (r'^anteriores/$','techtalks.views.anteriores'),
    (r'^fotos/$','techtalks.views.fotos'),
    (r'^fotos_edicao/(?P<edicao_id>\d+)/$','techtalks.views.fotos_edicao'),
    (r'^videos_e_slides_da_edicao/(?P<edicao_id>\d+)/$',
     'techtalks.views.videos_e_slides_da_edicao'),
    (r'^detalhes_edicao/(?P<edicao_id>\d+)/$','techtalks.views.detalhes_edicao'),
    (r'^detalhes_palestra/(?P<palestra_id>\d+)/$','techtalks.views.detalhes_palestra'),
    (r'^contato/$', 'techtalks.views.contato'),
    (r'^sucesso_contato/$','django.views.generic.simple.direct_to_template',
        {'template':'sucesso_contato.html'}),
    (r'^equipe/$','techtalks.views.equipe'),
    (r'^filtrar_por_tag/(?P<tag>[a-z0-9-]+)/$','techtalks.views.buscar_palestrar_por_tag'),
    
)

