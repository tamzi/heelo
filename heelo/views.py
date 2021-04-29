from django.shortcuts import render

# Create your views here.
def heelo(request):
    return render(request, 'heelo.html', {})
