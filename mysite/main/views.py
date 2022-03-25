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

def airpods(request):
    return render(request, 'airpods/airpods.html')

def specs(request):
    return render(request, 'airpods/specs.html')

def iphone(request):
    return render(request, 'main/iphone.html')
