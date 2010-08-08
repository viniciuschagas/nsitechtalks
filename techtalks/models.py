# -*- coding: utf-8 -*-
from datetime import date
from django.db import models

class Edicao(models.Model):
    STATUS = (
        ('pre_cadastro','Pré-Cadastro'),
        ('proxima','Próxima'),
        ('realizada','Realizada')
    )
    class Meta:
        ordering = ('-id',)
        
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
    palestras = models.ManyToManyField('Palestra')
    fotos = models.ManyToManyField('Foto',blank=True,null=True)
    videos = models.ManyToManyField('Video',blank=True,null=True)
    
    def __unicode__(self):
        titulo = str(self.id)+u'ª Edição - ('
        titulo += str(self.data.day)+'/'
        titulo += str(self.data.month)+'/'
        titulo += str(self.data.year)+')'
        return titulo
    
    def listar_palestras(self):
        return self.palestras.all()
    
    def listar_fotos(self):
        return self.fotos.all()
        
    def listar_videos(self):
        return self.videos.all()
        
    #TODO:Talvez transformar em um método de classe
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
    link_slideshare = models.CharField(
        verbose_name='link dos slides',
        max_length=1000
    )
    palavras_chave = models.ManyToManyField('PalavraChave')
    palestrantes = models.ManyToManyField('Palestrante')
    
    def __unicode__(self):
        return self.titulo
    
    def listar_palestrantes(self):
        return self.palestrantes.all()
        
    def listar_palavras_chave(self):
        return self.palavras_chave.all()
    
class Foto(models.Model):
    titulo = models.CharField(verbose_name='título',max_length=300)
    resumo = models.TextField(verbose_name='resumo',blank=True,null=True)
    arquivo = models.ImageField(
        verbose_name='arquivo',
        upload_to='imagens/fotos'
    )
    
    def __unicode__(self):
        return self.titulo

class Video(models.Model):
    titulo = models.CharField(verbose_name='título',max_length=300)
    resumo = models.TextField(verbose_name='resumo',blank=True,null=True)
    arquivo = models.CharField(
        verbose_name='link do vídeo',
        max_length=1000
    )
    
    def __unicode__(self):
        return self.titulo
    
class PalavraChave(models.Model):
    titulo = models.CharField(verbose_name='título',max_length=300)
    
    def __unicode__(self):
        return self.titulo
    
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
        upload_to='imagens/palestrantes'
    )
    site = models.CharField(
        verbose_name='site',
        max_length=400,
        blank=True,
        null=True
    )
    github = models.CharField(
        verbose_name='github',
        max_length=400,
        blank=True,
        null=True
    )
    twitter = models.CharField(
        verbose_name='twitter',
        max_length=400,
        blank=True,
        null=True
    )
    slideshare = models.CharField(
        verbose_name='slideshare',
        max_length=400,
        blank=True,
        null=True
    )
    
    def __unicode__(self):
        return self.nome