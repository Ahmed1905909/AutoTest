from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from nlpcloud import Client

def AutoTest(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
client = Client("fast-gpt-j", "", gpu=True)

@csrf_exempt
def generate_code(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        response = client.code_generation(text)
        return JsonResponse({'generated_code': response['generated_code']})
    else:
        return JsonResponse({'error': 'Invalid request method'})

