from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


import nlpcloud
from requests import HTTPError
import subprocess
import openai
openai.api_key = "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"

def home(request):
    if request.method == 'POST':
        input_text = request.POST['input_text']
        client = nlpcloud.Client("fast-gpt-j", "d41a09a6328bc4b5d21f34854efea91004d2cd3d", gpu=True)
        try:
            generated_code = client.code_generation(input_text)
        except HTTPError as e:
            if e.response.status_code == 429:
                error_message = "Error: Too many requests. Please try again later or contact support."
            else:
                error_message = "Error: {}".format(e)
            return render(request, 'gp/home.html', {'error_message': error_message, 'input_text': input_text})
        return render(request, 'gp/home.html', {'generated_code': generated_code, 'input_text': input_text})
    else:
        return render(request, 'gp/home.html')

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
def logino(request):
    return render(request, 'users/LogIn.html')
def siginup(request):    
    return render(request, 'users/register.html')
def lm(request):
    return render(request, 'gp/learnMore.html')
def userpage(request):
    return render(request, 'gp/peofile.html')
def history(request):
    return render(request, 'gp/history.html')
def chat(request):
    context = {}

    if request.method == "POST":
        function_input = request.POST.get("function_input")
        if function_input:
            prompt = f"you are a world class test case generator generate test cases for the following function: {function_input}"

            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                temperature=0.5,
                max_tokens=100
            )

            test_cases = response.choices[0].text

            context["function_input"] = function_input
            context["test_cases"] = test_cases

    return render(request, "gp/chat.html", context=context)
