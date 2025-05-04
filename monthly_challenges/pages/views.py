from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render


def page_not_found(request: HttpRequest, exception: Http404) -> HttpResponse:
    return render(request, 'pages/404.html', status=404)
