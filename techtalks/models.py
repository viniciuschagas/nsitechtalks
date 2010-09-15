# -*- coding: utf-8 -*-
from datetime import date
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from utils.pyslideshare.pyslideshare import pyslideshare
from utils.pyslideshare_configurations import API_KEY, SECRET_KEY

class Edicao(models.Model):
    STATUS = (
        ('pre_cadastro','Pré-Cadastro'),
        ('proxima','Próxima'),
        ('realizada','Realizada')
    )
    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'Edições'
        
    data = models.DateField(verbose_name='data')
    hora = models.TimeField(verbose_name='hora')
    local = models.CharField(verbose_name='local',max_length=150)
    cartaz = models.ImageField(
        verbose_name='cartaz',
        upload_to='imagens/cartazes'
    )
    status = models.CharField(
        verbose_name='status',
        max_length=12,
        choices=STATUS,
        default='pre_cadastro')
    
    def __unicode__(self):
        titulo = str(self.id)+u'ª Edição - ('
        titulo += str(self.data.day)+'/'
        titulo += str(self.data.month)+'/'
        titulo += str(self.data.year)+')'
        return titulo
    
    def listar_palestras(self):
        return self.palestra_set.all()
    
    def listar_fotos(self):
        return self.foto_set.all()
        
    def listar_videos(self):
        return self.video_set.all()
        
    def _retirar_outras_como_proxima(self):
        edicoes = Edicao.objects.all()
        for edicao in edicoes:
            if (edicao.status == 'proxima') or (edicao.data < date.today()):
                edicao.status = 'realizada'
                edicao.save()
        
    def save(self, *args,**kwargs):
        if self.status == 'proxima':
            self._retirar_outras_como_proxima()
        super(Edicao,self).save(*args,**kwargs)

class Palestra(models.Model):
    titulo = models.CharField(verbose_name='título',max_length=300)
    resumo = models.TextField(verbose_name='resumo')
    edicao = models.ForeignKey(Edicao)
    id_slideshare = models.IntegerField(
        verbose_name='Id dos slides',
        null=True,
        blank=True
    )
    palavras_chave = models.ManyToManyField('PalavraChave')
    palestrantes = models.ManyToManyField('Palestrante')
    
    def __unicode__(self):
        return self.titulo
    
    def listar_palestrantes(self):
        return self.palestrantes.all()
        
    def listar_palavras_chave(self):
        return self.palavras_chave.all()
        
    def listar_videos(self):
        return self.video_set.all()
        
    def retornar_slide_embeded(self):
        api_key = API_KEY
        secret_key = SECRET_KEY
        slides_client = pyslideshare(locals(),verbose=False)
        slide = slides_client.get_slideshow(slideshow_id=self.id_slideshare)
        location = slide.items()[0][1]['Slideshow']['Location']['value']
        embed_code = '<object id="__sse%s" width="350" height="292">\
                        <param name="movie"\
                            value="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc=%s&stripped_title=a" />\
                        <param name="allowFullScreen" value="true"/>\
                        <param name="allowScriptAccess" value="always"/>\
                        <embed name="__sse%s"\
                            src="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc=%s&stripped_title=a"\
                            type="application/x-shockwave-flash"\
                            allowscriptaccess="always"\
                            allowfullscreen="true"\
                            width="350"\
                            height="292">\
                        </embed>\
                    </object>' % (self.id_slideshare, location, self.id_slideshare, location)
        slide_url = slide.items()[0][1]['Slideshow']['Permalink']['value']
        return (embed_code,slide_url)
    
class Foto(models.Model):
    titulo = models.CharField(verbose_name='título',max_length=300)
    resumo = models.TextField(verbose_name='resumo',blank=True,null=True)
    edicao = models.ForeignKey(Edicao)
    arquivo = models.ImageField(
        verbose_name='arquivo',
        upload_to='imagens/fotos'
    )
    
    def __unicode__(self):
        return self.titulo

class Video(models.Model):
    titulo = models.CharField(verbose_name='título',max_length=300)
    resumo = models.TextField(verbose_name='resumo',blank=True,null=True)
    edicao = models.ForeignKey(Edicao)
    palestra = models.ForeignKey(Palestra,blank=True,null=True)
    id_video = models.CharField(
        verbose_name='Id do vídeo',
        max_length=15
    )
    
    def __unicode__(self):
        return self.titulo
    
    def retornar_embed(self):
        return '<iframe src="http://player.vimeo.com/video/%s?portrait=0"\
                width="350" height="197"\
                frameborder="0"></iframe>' % self.id_video
    
class PalavraChave(models.Model):
    titulo = models.CharField(verbose_name='título',max_length=300)
    slug = models.SlugField(max_length=300, blank=True, null=True)
    
    def __unicode__(self):
        return self.titulo
        
def palavra_chave_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)
    
signals.pre_save.connect(palavra_chave_pre_save, sender=PalavraChave)
    
class Palestrante(models.Model):
    nome = models.CharField(verbose_name='nome',max_length=100)
    o_que_faz = models.TextField(verbose_name='o que faz')
    resumo = models.TextField(
        verbose_name='resumo da vida e obra',
        blank=True,
        null=True
    )
    foto = models.ImageField(
        verbose_name='foto',
        upload_to='imagens/palestrantes',
        default='imagens/default_palestrante.png'
    )
    site = models.URLField(
        verbose_name='site',
        max_length=400,
        blank=True,
        null=True,
        verify_exists=False
    )
    github = models.URLField(
        verbose_name='github',
        max_length=400,
        blank=True,
        null=True,
        verify_exists=False
    )
    twitter = models.URLField(
        verbose_name='twitter',
        max_length=400,
        blank=True,
        null=True,
        verify_exists=False
    )
    slideshare = models.URLField(
        verbose_name='slideshare',
        max_length=400,
        blank=True,
        null=True,
        verify_exists=False
    )
    
    def __unicode__(self):
        return self.nome
