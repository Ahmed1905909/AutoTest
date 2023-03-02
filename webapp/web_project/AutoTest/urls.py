from django.urls import path
from .views import generate_test_cases
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('AutoTest/', views.AutoTest, name='AutoTest'),
    path('generate_test_cases/', views.generate_test_cases, name='generate_test_cases'),

]

urlpatterns += staticfiles_urlpatterns()




#urlpatterns = [
   # path('', include('web_project.urls')),
   # path('admin/', admin.site.urls),
#]
