from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Ip_addr(models.Model):
    ip_addr = models.CharField(max_length=200)

    def __str__(self):
        return self.ip_addr

class Question(models.Model):
    question_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Freetext(models.Model):
    free_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.free_text
