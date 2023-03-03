from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


import nlpcloud

def AutoTest(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def signin_view(request):
    return render(request, 'signin.html')

def generate_test_cases(request):
    if request.method == 'POST':
        prompt = request.POST['prompt']
        client = nlpcloud.Client("fast-gpt-j", "5057a9c100a6388bfc382dfad671982ed6b52733", gpu=True)
        generated_code = client.code_generation(f"""Generate Java test cases in JUnit form for {prompt}""")
        return render(request, 'generated_message.html', {'generated_message': generated_code})
    else:
        return render(request, 'generate_test_cases.html')