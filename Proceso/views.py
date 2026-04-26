from django.shortcuts import render

# Create your views here.
def homeProcesos(request):
    return render(request, 'cliente/index.html')