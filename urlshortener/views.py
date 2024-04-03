from django.shortcuts import render
from . forms import UrlShortenForm

# Create your views here.
def urlshortener(request):
    form = UrlShortenForm(request.POST or None)

    context={
        'form':form,
    }
    return render(request, 'urlshortener/urlshortener.html', context)
