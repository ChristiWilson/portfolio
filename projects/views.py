from django.shortcuts import render

from .models import Project


def home_view(request):
    return render(request, "home.html")


def project_list(request):
    projects = Project.objects.all()
    context = {
            "projects": projects,
            }
    return render(request, "project_list.html", context)


def project_detail(request, p_id):
    project = Project.objects.get(id=p_id)
    context = {
            "project": project,
            }
    return render(request, "project_detail.html", context)
