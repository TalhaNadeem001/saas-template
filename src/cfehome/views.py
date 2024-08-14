from django.shortcuts import render
from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    page_heading = 'Saas'
    context = {
        'page': page_heading,
        'page_visits': page_qs.count(),
        'total_visits': queryset.count()
    }
    PageVisit.objects.create(path=request.path)
    return render(request, 'home.html', context)