from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request, 'third_app/index.html', context=context_dict)


def other(request):
    return render(request, 'third_app/other.html')


def relative(request):
    return render(request, 'third_app/relative_url.html')
