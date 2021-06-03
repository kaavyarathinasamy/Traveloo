from django.shortcuts import render
from django.http import HttpResponse
from . models import Destination
# Create your views here.
def index(request):
    # dest1= Destination()
    # dest1.id=1
    # dest1.name='Bangalore'
    # dest1.img='destination_1.jpg'
    # dest1.desc='Everywhere Pubs and IT'
    # dest1.price=10000
    # dest1.spl_offer=False

    # dest2= Destination()
    # dest2.id=2
    # dest2.name='Coimbatore'
    # dest2.img='destination_2.jpg'
    # dest2.desc='Piece of pease and a bit of nature'
    # dest2.price=5000
    # dest2.spl_offer=True

    # dest3= Destination()
    # dest3.id=2
    # dest3.name='Kerela'
    # dest3.img='destination_3.jpg'
    # dest3.desc='Gods own place'
    # dest3.price=15000
    # dest3.spl_offer=False

    # dests = [dest1,dest2,dest3]

    dests=Destination.objects.all()

    return render(request,'index.html',{'dests':dests})


