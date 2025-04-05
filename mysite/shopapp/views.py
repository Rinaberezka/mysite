from timeit import default_timer
# from http.client import HTTPResponse
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
# from django.template import loader


def shop_index(request):
    context = {
        "time_running": default_timer(),
    }
    return render(request,'shopapp/shop_index.html', context=context)

def about_us(request):
    return render(request,"shopapp/about.html")