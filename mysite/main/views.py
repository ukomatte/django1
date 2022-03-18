from django.shortcuts import render


def index(request):
    data = {
        'title': 'Main page'
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')

def backend(request):
    return render(request, 'main/backend.html')

def product(request):
    return render(request, 'main/product.html')

def product(request):
    return render(request, 'main/airpods.html')
