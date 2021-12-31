from django.http import Http404, HttpResponse
import datetime


def start_page(request):
    return HttpResponse('Это стартовая страница, для демострации работы URL.')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Сейчас %s </body></html>" %now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        _offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours = _offset)
    assert True
    html = "<html><body>Через %s часов будет %s</body><html>" % (offset, dt)
    return HttpResponse(html)