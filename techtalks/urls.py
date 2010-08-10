from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$','techtalks.views.index'),
    (r'^palestrante/(?P<palestrante_id>\d+)/$','techtalks.views.palestrante'),
)

