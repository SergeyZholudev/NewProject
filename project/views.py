from django.http import HttpResponse
import datetime


def hello(request):
    return HttpResponse('This is example of using view.py as function.')


def start_page(request):
    return HttpResponse('Это стартовая страница, для демострации работы URL.')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Сейчас %s </body></html>" %now
    return HttpResponse(html)
    