from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def index(request):
    context = {
        'time': strftime('%H:%M %p', gmtime()),
        'date': strftime('%b %d, %Y')
    }
    return render(request, 'appDisplay/index.html', context)


