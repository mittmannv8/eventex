# -*- coding: utf-8 -*-
from django.db import models

class Contato(models.Model):
    nome = models.CharField('Nome',max_length=100)
    cpf = models.CharField('CPF',max_length=11,unique=True)
    email = models.EmailField('E-mail',unique=True)
    telefone = models.CharField('Telefone',max_length=20,blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ['data_criacao']
        verbose_name = u'Inscrição'
        verbose_name_plural = u'Inscrições'
