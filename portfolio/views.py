from django.shortcuts import render
from .models import Portfolio

def home(reguest):
    return render(reguest, 'home.html')

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios':portfolios})
