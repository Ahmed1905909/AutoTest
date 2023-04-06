from django.shortcuts import render
from django.http import HttpResponse
import nlpcloud
from requests import HTTPError
import subprocess

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

