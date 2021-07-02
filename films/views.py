from django.shortcuts import render
from django.utils import timezone
from .models import FilmsToWatch

def post_list(request):
    Films = FilmsToWatch.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'films/post_list.html', {'Films': Films})
