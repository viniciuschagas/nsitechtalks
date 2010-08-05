# -*- coding: utf-8 -*-
from django.db import models

class Edicao(models.Model):
    data = models.DateField(verbose_name='data')
    hora = models.TimeField(verbose_name='hora')
    local = models.CharField(verbose_name='local',max_length=150)
    cartaz = models.ImageField(
        verbose_name='cartaz',
        upload_to='imagens/cartazes'
    )
    palestras = models.ForeignKey('Palestra')
    fotos = models.ForeignKey('Foto')
    videos = models.ForeignKey('Video')
    
    def __unicode__(self):
        titulo = str(self.id)+'ª Edição - ('
        titulo += str(self.data.day)+'-'
        titulo += str(self.data.month)+'-'
        titulo += str(self.data.year)+')'
        return titulo
    
    def listar_palestras(self):
        return self.palestras_set.all()
    
    def listar_fotos(self):
        return self.fotos_set.all()
        
    def listar_videos(self):
        return self.videos_set.all()

class Palestra(models.Model):
    titulo = models.CharField(verbose_name='título',max_length=300)
    resumo = models.TextField(verbose_name='resumo')
    link_slideshare = models.CharField(
        verbose_name='link dos slides',
        max_length=1000
    )
    palavras_chave = models.ForeignKey('PalavraChave')
    palestrantes = models.ManyToManyField('Palestrante')
    
class Foto(models.Model):
    titulo = models.CharField(verbose_name='título',max_length=300)
    resumo = models.TextField(verbose_name='resumo',blank=True,null=True)
    arquivo = models.ImageField(
        verbose_name='arquivo',
        upload_to='imagens/fotos'
    )

class Video(models.Model):
    titulo = models.CharField(verbose_name='título',max_length=300)
    resumo = models.TextField(verbose_name='resumo',blank=True,null=True)
    arquivo = models.CharField(
        verbose_name='link do vídeo',
        max_length=1000
    )
    
class PalavraChave(models.Model):
    titulo = models.CharField(verbose_name='título',max_length=300)
    
class Palestrante(models.Model):
    nome = models.CharField(verbose_name='nome',max_length=100)
    o_que_faz = models.CharField(verbose_name='o que faz',max_length=300)
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