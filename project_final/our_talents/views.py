from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Our_talents

def our_talents(request):
    talent = Our_talents.objects.all()
    paginator = Paginator(talent, 4)

    page = request.GET.get('page')
    our_talents = paginator.get_page(page)
    return render(request, 'our_talents/our_talents.html', {'talents': our_talents})