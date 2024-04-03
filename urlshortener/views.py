from django.shortcuts import render, redirect
from . forms import UrlShortenForm
from . models import ShortenedURL
import pyshorteners
import requests
from requests.exceptions import ReadTimeout


# Create your views here.
def urlshortener(request):
    form = UrlShortenForm(request.POST or None)
    shortened_url = None
    original_url = None

    if request.method=="POST":
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            s = pyshorteners.Shortener()
            try:
                shortened_url = s.tinyurl.short(original_url)
            except ReadTimeout:
                try:
                    shortened_url= s.bitly.short(original_url)
                except ReadTimeout:
                    pass



    context={
        'form':form,
        'shortened_url':shortened_url,
        'original_url':original_url,
    }

    return render(request, 'urlshortener/urlshortener.html', context)
