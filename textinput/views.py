from django.shortcuts import render

# Create your views here.
def text2(request):
    return render(request, 'text2.html', {})