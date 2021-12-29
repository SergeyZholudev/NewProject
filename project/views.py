from django.http import HttpResponse

def hello(request):
    return HttpResponse('This is example of using view.py as function.')