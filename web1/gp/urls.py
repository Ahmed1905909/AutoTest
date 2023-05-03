from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('siginup', views.siginup, name='siginup'),
    path('lm', views.lm, name='lm'),
    path('up', views.up, name='up'),
    path('chat', views.chat, name='chat'),
    path('java', views.Java, name='java'),
    path('call',views.call_java_method, name = 'javaa'),
    path('genetic', views.upload, name='genetic')
]
