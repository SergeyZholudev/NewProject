from django.shortcuts import render
from django.http import Http404, HttpResponse
import datetime


def start_page(request):
    return HttpResponse('Это стартовая страница, для демострации работы URL.')

def current_datetime(request):
    now = datetime.datetime.now()
    return render( request, 'time_templates/current_datetime.html', {'current_datetime': now} )

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
    return render(request, 'time_templates/time_offset.html', {'next_time': dt, 'offset': offset})