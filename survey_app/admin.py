from django.contrib import admin
from .models import Question, Choice, Freetext, Ip_addr

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Freetext)
admin.site.register(Ip_addr)