from django.urls import path, register_converter

from . import converters, views

app_name = 'challenges'

register_converter(converters.TwoDigitYearConverter, "dd")

urlpatterns = [
    path('', views.index, name='index'),
    path('<dd:month>/', views.monthly_challenges_num, name='monthly-challenges-num'),
    path('<str:month>/', views.monthly_challenges, name='monthly-challenges'),
]
