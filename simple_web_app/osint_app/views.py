from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from django.http import StreamingHttpResponse
from .forms import PostForm
from .modules import start
from .modules.search_subdomains import DATE
import os
import mimetypes
from datetime import datetime, date


# Create your views here.
def data_collect(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data['name_of_organization']
            domains = form.cleaned_data['domains']
            url = "./report/?name={}&dom={}".format(name, domains)
            return HttpResponseRedirect(url)
    else:
        form = PostForm()
    return render(request, './data_collection/collection.html', {'form': form})


def waiting(request):
    if request.method == "GET":
        name = request.GET.get('name')
        domain = request.GET.get('dom')
        print(domain)
        start.main(name, domain)
        return render(request, "./data_collection/waiting.html", {'name': name, 'domains': domain})


def report(request):
    if request.method == "GET":
        name = request.GET.get('name')
        domain = request.GET.get('dom')
        print(domain)
        # inn = request.GET.get('inn')
        start.main(name, domain)
        filename = f"{domain}-{DATE}.csv"
    return render(request, './data_collection/report.html', {'name': name, 'domains': domain, 'filename': filename})


def download_file(request, filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(BASE_DIR+"/reports/", filename), 'rb') as f:
        data = f.read()
    response = HttpResponse(data)
    response['Content-Disposition'] = f'attachment; filename={filename}'
    return response