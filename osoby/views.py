from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Witaj w Django!")


def onas(request):
    return HttpResponse("<h1>informacje o nas</h1>")
