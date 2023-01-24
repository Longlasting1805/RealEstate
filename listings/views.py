from django.shortcuts import render
from .models import Listing
# Create your views here.

def home(request):
    listings = Listing.objects.all()
    return render(request, 'listings/home.html', {'listings': listings})
