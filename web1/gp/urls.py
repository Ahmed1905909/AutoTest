from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< Updated upstream
    path('logino', views.logino, name='logino'),
    path('siginup', views.siginup, name='siginup'),
=======
    path('login', views.login, name='login'),
    path('siginup', views.siginup, name='register'),
>>>>>>> Stashed changes
    path('lm', views.lm, name='lm'),
    path('userpage', views.userpage, name='userpage'),
    path('history', views.history, name='history'),
    path('chat', views.chat, name='chat'),
    path('index/', views.index, name='gp-index'),
    path('java', views.Java, name='java'),
    path('call',views.call_java_method, name = 'javaa'),
<<<<<<< Updated upstream
    path('genetic', views.upload, name='genetic')
]
=======
    path('genetic', views.upload, name='genetic'),
    path('ovth', views.run_java_program, name='run_java_program'),

]
>>>>>>> Stashed changes
