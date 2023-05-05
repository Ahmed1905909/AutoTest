from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logino', views.logino, name='logino'),
    path('siginup', views.siginup, name='siginup'),
    path('lm', views.lm, name='lm'),
    path('userpage', views.userpage, name='userpage'),
    path('history', views.history, name='history'),
    path('chat', views.chat, name='chat'),
    path('index/', views.index, name='gp-index'),
    path('java', views.Java, name='java'),
    path('call',views.call_java_method, name = 'javaa'),
    path('genetic', views.upload, name='genetic')
]