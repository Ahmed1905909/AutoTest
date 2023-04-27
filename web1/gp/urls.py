from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='lol'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('siginup', views.siginup, name='siginup'),
    path('lm', views.lm, name='lm'),
    path('chat', views.chat, name='chat'),
]
