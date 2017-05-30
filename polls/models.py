# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from spaces.models import Space
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=254)
    pub_date = models.DateTimeField()
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question_text
    
    def __unicode__(self):
        return self.question_text
    
    class Meta:
        ordering = ["pub_date"]
        

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=254)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
    def __unicode__(self):
        return self.choice_text
    
    class Meta:
        ordering = ["question"]