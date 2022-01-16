from django.shortcuts import render
from .models import rca, gliit, tfcc, ci, svi     

def home(request):
    page_title = 'Home'
    rca_count = rca.objects.all().count()
    gliit_count = gliit.objects.all().count()
    ci_count = ci.objects.all().count()
    svi_count = svi.objects.all().count()
    tfcc_count = tfcc.objects.all().count()

    context = {
        'page_title' : page_title,
        'rca_count' : rca_count,
        'gliit_count' : gliit_count,
        'ci_count' : ci_count,
        'svi_count' : svi_count,
        'tfcc_count' : tfcc_count
    }
    return render(request, 'home.html', context)

def about(request):
    page_title = 'About'
    return render(request, 'about.html', { 'page_title':page_title })

