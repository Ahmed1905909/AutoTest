from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
import nlpcloud
from requests import HTTPError
import subprocess
import openai
import jpype
from my_module import genetic_algorithm
from jpype import *
openai.api_key = "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"



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


def Java(request):
    return render(request, 'gp/Java.html')


def java_view(request):
    if request.method == 'POST':
        # Retrieve user input from the form
        input_value = request.POST.get('input_value')

        # Call the Java function using subprocess
        process = subprocess.Popen(['java', 'MyJavaClass', input_value],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Process the output of the Java function
        output = stdout.decode('utf-8')

        # Render the output in the template
        return render(request, 'output.html', {'output': output})

    return render(request, 'input_form.html')




def call_java_method(request):
    print("HI")
    jpype.startJVM()
    classpath = "D:\\Grad2.0\\finalfinal"

    jpype.addClassPath(classpath)
    print(jpype.getClassPath())
    print("HI3")

    class_loader = jpype.JClass('java.lang.Thread').currentThread().getContextClassLoader()

    # Load the class using the classloader
    my_class = class_loader.loadClass("src\\FunctionExtractor.java")
    print("HI9")

    # Create an instance of the class
    my_instance = my_class()

    # Call a method on the instance
    my_instance.my_method()
    print(my_class)
    print("HI2")
    # Shutdown the JVM
    jpype.shutdownJVM()
    # create a Pype interface for the Java class that contains the method you want to call
    # java_class = jpype.JClass("FunctionExtractor.java")


    # # create an instance of the Java class
    # java_instance = java_class()
    # print(result)
    # # call the method on the Java class instance
    # result = java_instance.Main()
    # print(java_instance)
    # return the result as an HTTP response
    return render(request, 'gp/output.html')
    #return HttpResponse(result)




def upload(request):
    if request.method == 'POST':
        name = request.POST['name']
        file1 = request.FILES['file1']
        file2 = request.FILES['file2']

        result = genetic_algorithm.crossover()

        #return HttpResponse(result)

    return render(request, 'gp/genetic.html')
