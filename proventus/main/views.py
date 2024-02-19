from django.shortcuts import render
from .models import *
# Create your views here.


def main_page(request):
    sevices=Services.objects.all()
    context={
        "services":sevices
    }
    return render(request, 'index.html', context)
