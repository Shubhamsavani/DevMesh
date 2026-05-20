from .models import Tag, Project
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger

def search_projects(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query= request.GET.get('search_query')
    tag = Tag.objects.filter(name__icontains = search_query)

    project=Project.objects.distinct().filter(
        Q(title__icontains = search_query) | 
        Q(description__icontains = search_query) |
        Q(tags__in = tag) |
        Q(owner__name__icontains = search_query)
    )
    return [project, search_query]
def pagination(request, projects):
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(projects, results)
    try:
        projects= paginator.page(page)
    except PageNotAnInteger:
        page=1
        projects= paginator.page(page)
    except EmptyPage:
        page=paginator.num_pages
        projects = paginator.page(page)
    return [projects, paginator.page_range, paginator ]

# 6250 