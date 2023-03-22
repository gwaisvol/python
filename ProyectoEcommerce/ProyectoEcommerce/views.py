from django.http import HttpResponse
from django.shortcuts import render

def welcome_page(request):
    return render(request, 'welcome.html', context={})

def our_company(request):
    return render(request, 'us.html', context={})

