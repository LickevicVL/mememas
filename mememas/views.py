from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


# def handler404(request):
#