from django.shortcuts import render
from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    page_heading = 'Saas'
    context = {
        'page': page_heading,
        'visits': queryset.count()
    }
    PageVisit.objects.create(path=request.path, )
    return render(request, 'home.html', context)