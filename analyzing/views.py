from django.shortcuts import render

# Create your views here.
def text3(request):
    return render(request, 'text3.html', {})