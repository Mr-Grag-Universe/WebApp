from django.http import HttpResponseRedirect
from django.shortcuts import render

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

# Create your views here.


def index(request):
    data = {
        'title': 'Главная страница',
        'value': ['some', 'hello', 1],
    }
    return render(request, 'main/index.html', data)
