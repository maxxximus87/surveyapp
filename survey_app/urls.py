from django.conf.urls import url
from . import views

app_name = 'survey_app'
urlpatterns = [

    # ex: /survey_app/
    url(r'^$', views.index, name='index'),

    # ex: /survey_app/
    url(r'^detail/$', views.detail, name='detail'),

    # ex: /survey_app/
    url(r'^submit/', views.submit, name='submit'),

    url(r'^vote/$', views.vote, name='vote'),

]