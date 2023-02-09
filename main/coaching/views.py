from django.shortcuts import render
from .forms import ClientForm
from .models import SportTag

# Create your views here.

def main_page(request):
    return render(request, "coaching/index.html")

def posts(request):
    return render(request, "coaching/post.html")


def requests(request):    
    return render(request, "coaching/about.html", context={"db": SportTag.objects.all()})

def form(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.data.values()
            print(list(data), type(data))
        else:
            print('IDI NAHUY')
    else:
        form = ClientForm()
    return render(request, "coaching/contact.html", context={'form': form})