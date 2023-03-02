from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader



def AutoTest(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
