from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View


# Create your views here.
class Money(View):
    def get(self, request):
        return render(request, 'money/index.html')
