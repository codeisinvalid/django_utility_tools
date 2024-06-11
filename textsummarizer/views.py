from django.shortcuts import render

# Create your views here.
def summarizer(request):
    return render(request, 'textsummarizer/textsummarizer.html')