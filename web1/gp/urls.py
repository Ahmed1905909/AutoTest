from django.urls import path
from . import views

urlpatterns = [
    path('gome', views.home, name='lol'),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('siginup', views.siginup, name='siginup'),
    path('lm', views.lm, name='lm'),
    path('up', views.up, name='up'),
    path('chat', views.chat, name='chat'),
]
