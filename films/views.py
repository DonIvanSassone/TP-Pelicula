from django.shortcuts import render
from django.utils import timezone
from .models import FilmsToWatch

def post_list(request):
    allFilms = FilmsToWatch.objects.filter(Year__lte=timezone.now()).order_by('Year')
    return render(request, 'films/post_list.html', {'allFilms': allFilms})
