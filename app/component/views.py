from django.shortcuts import render
from .models import Card

# Create your views here.


def card(request):
    new = Card.objects.all()
    
    return render(request , "component/card.html")