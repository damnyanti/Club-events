from django.shortcuts import render
from django.http import HttpResponse
from .models import Club
from django.shortcuts import render , get_object_or_404
from django.contrib.auth.decorators import login_required

CLUB_NAMES = {

    "codingclubiitg":"Coding Club",
    'robotics.iitg':'Robotics',
    'electronics.iitg':'Electronics',
    'Aeroiitg':'Aeromodelling',
    'litsociitg':'LitSoc',
    'iitgai':'IITG.AI',
    'xpressionsiitg':'Xpressions',
    'cadence.iitg':'Cadence',
}
@login_required(login_url="/login/")
def index(request):
    all_clubs = Club.objects.all()
    context = {'all_clubs': all_clubs}
    return render(request, 'clubs.html', context)

@login_required(login_url="/login/")
def detail(request, club_Id):
    club_ = get_object_or_404(Club, club_id= club_Id)
    return render(request, 'detail.html', {'club': club_ })
    # club_oname  = CLUB_NAMES[club_name]
    # return render(request, 'detail.html', {'club_name':club_oname})

