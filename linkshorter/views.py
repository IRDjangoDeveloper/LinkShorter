from django.shortcuts import render, redirect
from .forms import userlink
from django.contrib import messages
import random
import string
from .models import links
# Create your views here.
def link_shorter(request):
    form = userlink(request.POST)
    if request.method == 'GET':
        return render(request, 'form_home.html', {'form':form})

    if request.method == 'POST':
        form = userlink(request.POST)
        if form.is_valid():
            link_user = form.cleaned_data.get('input')
            shorted = random.randint(11111, 99999)
            query = links.objects.create(link=link_user, short=shorted)
            messages.info(request, f'http://localhost:8000/s/{shorted}')
            return redirect('/')

def redirector(request, *args, **kwargs):
    linked = kwargs.get('args')
    redirect_link = links.objects.get(short__iexact=linked)
    if redirect_link:
        return redirect(redirect_link.link)
    return redirect('/')