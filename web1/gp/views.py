from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from requests import HTTPError
import subprocess
import openai
import jpype
import json
import os
from .test_suite_mang.test_suite_manger import run_test_suite
#from my_module import genetic_algorithm
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
        Jason = request.POST['Json']
        file2 = request.FILES['file2']
        file_path = os.path.join(os.getcwd(), 'uploads', file2.name)
        with open(file_path, 'wb') as destination_file:
            for chunk in file2.chunks():
                destination_file.write(chunk)
        # TODO: Optionally do some processing on the file contents here

        result = run_test_suite(name, json.loads(Jason) , None)

        return render(request, 'gp/'+result)

    return render(request, 'gp/genetic.html')


def run_java_program(request):
    # Path to the Java program
    java_program = "D:\\Grad2.0\\finalfinal\\out\\production\\finalfinal\\"

    # Arguments to be passed to the Java program
    arguments = "arg1"

    # Call the Java program using subprocess
    result = subprocess.run(["java", "FunctionExtractor",java_program,arguments] , stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Check if the Java program executed successfully
    if result.returncode == 0:
        # If successful, return the output
        return HttpResponse(result.stdout)
    else:
        # If there was an error, return the error message
        return HttpResponse(result.stderr)