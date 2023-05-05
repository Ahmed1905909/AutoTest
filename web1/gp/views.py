from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


import nlpcloud
from requests import HTTPError
import subprocess
import openai
openai.api_key = ""


def handle_file_upload(request):
    # Handle the file upload using Django's built-in functionality
    uploaded_file = request.FILES['file']

    # Call the Java program using subprocess
    result = subprocess.run(['java', 'MyJavaProgram', uploaded_file.name],
                        cwd='/path/to/java/program',  # replace with the path to your Java program
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    # Capture the output of the Java program
    output = result.stdout.decode('utf-8')

    # Return the output as a response
    return HttpResponse(output)
def index(request):
    return render(request, 'gp/index.html')
def login(request):
    return render(request, 'users/LogIn.html')
def siginup(request):    
    return render(request, 'users/register.html')
def lm(request):
    return render(request, 'gp/learnMore.html')
def up(request):
    return render(request, 'gp/peofile.html')
def chat(request):
    context = {}

    if request.method == "POST":
        function_input = request.POST.get("function_input")
        language = request.POST.get("language")
        if function_input:
            prompt = f"you are a world class test case generator generate test cases for the following {language}function: {function_input}"

            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                temperature=0.5,
                max_tokens=100
            )

            test_cases = response.choices[0].text

            context["function_input"] = function_input
            context["test_cases"] = test_cases
            context["language"]=language

    return render(request, "gp/chat.html", context=context)
