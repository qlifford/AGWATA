from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.
class Snapy(View):
    def get(self, request):
        return render(request, 'snapy/gallery.html')
        
class Gallery(View):
    def get(self, request):
        return render(request, 'snapy/details.html')

class Add(View):
    def get(self, request):
        return render(request, 'snapy/add.html')