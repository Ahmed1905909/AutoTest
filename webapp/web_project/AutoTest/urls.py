from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('AutoTest/', views.AutoTest, name='AutoTest'),
]
urlpatterns += staticfiles_urlpatterns()