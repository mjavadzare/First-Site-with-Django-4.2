from django.shortcuts import render,get_object_or_404 , HttpResponseRedirect, redirect

from django.utils import timezone
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def projects_view(request, *args, **kwargs):
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
    # pagination
    projects = Paginator(projects, 3)
    try :
        page_number = request.GET.get('page')
        projects = projects.get_page(page_number)
    except PageNotAnInteger:
        projects = projects.get_page(1)
    except EmptyPage:
        projects = projects.get_page(1)

    context={'projects': projects}
    return render(request, 'project/project.html', context)



def projects_single_view(request, pid):
    project = get_object_or_404(Project, pk=pid , published_date__lte=timezone.now())
    related_projects = Project.objects.filter(type=project.type)
    context = {'project': project , 'related_projects':related_projects , }
    return render(request, 'project/project_details.html', context)