from django.shortcuts import render
from hierarchical_app.models import Folder
# Create your views here.


def index_view(request):
    return render(request, 'index.html', {'welcome': "Welcome to Kens Hierarchical Data and You assessment", 'folders': Folder.objects.all()})

