from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hw_lesson_4(request):
    return HttpResponse('Домашка по 4 заданию')