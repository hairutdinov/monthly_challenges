from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello World')

def monthly_challenges(request: HttpRequest, month: str) -> HttpResponse:
    return HttpResponse(f'Current month: {month}')

def monthly_challenges_num(request: HttpRequest, month: int) -> HttpResponse:
    return HttpResponse(f'Current month number: {month}')