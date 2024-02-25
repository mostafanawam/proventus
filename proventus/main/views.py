from django.shortcuts import render
from .models import *
# Create your views here.


def main_page(request):
    sevices=Services.objects.all().order_by('index')
    company=Company.objects.first()
    links=SocialLinks.objects.all()
    context={
        "services":sevices,
        "company":company,
        "links":links
    }
    return render(request, 'index.html', context)
