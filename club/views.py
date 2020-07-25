from django.shortcuts import render
from django.http import HttpResponse
from .models import Club


def index(request):
    all_clubs = Club.objects.all()
    context = {'all_clubs': all_clubs}
    return render(request, 'clubs.html', context)

