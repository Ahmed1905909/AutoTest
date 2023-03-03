from django.urls import path
from .views import generate_test_cases
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import include, path
from .views import signin_view
urlpatterns = [
    path('AutoTest/', views.AutoTest, name='AutoTest'),
    path('generate/', views.generate_test_cases, name='generate_test_cases'),
    path('signin/', signin_view, name='signin'),
]



urlpatterns += staticfiles_urlpatterns()




#urlpatterns = [
   # path('', include('web_project.urls')),
   # path('admin/', admin.site.urls),
#]
