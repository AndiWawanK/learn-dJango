from django.shortcuts import render
from django.http import HttpResponse


def hometest(request):
    return HttpResponse('halooo keindahan alam')
