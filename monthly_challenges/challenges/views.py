from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, \
    Http404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_safe
from django.urls import reverse


MONTHLY_CHALLENGES = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None,
}

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'challenges/index.html', {
        'obejcts_list': list(MONTHLY_CHALLENGES.keys())
    })

@require_http_methods(['GET'])
def monthly_challenges(request: HttpRequest, month: str) -> HttpResponse:
    try:
        return render(request, 'challenges/challenge.html', {
            'month': month,
            'challenge': MONTHLY_CHALLENGES[month]
        })
    except KeyError:
        raise Http404('This month is not supported')

@require_safe
def monthly_challenges_num(request: HttpRequest, month: int) -> HttpResponse:
    try:
        month_name = list(MONTHLY_CHALLENGES.keys())[month - 1]
    except IndexError:
        return HttpResponseNotFound('This month is not supported')
    return redirect(reverse('challenges:monthly-challenges', args=[month_name]))