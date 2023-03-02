from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('AutoTest/', views.AutoTest, name='AutoTest'),
]

urlpatterns += staticfiles_urlpatterns()




#urlpatterns = [
   # path('', include('web_project.urls')),
   # path('admin/', admin.site.urls),
#]
