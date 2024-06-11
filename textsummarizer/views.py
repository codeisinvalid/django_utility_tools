# summarizer/views.py
from django.shortcuts import render
from .forms import TextForm
from .utils import TextSummarizer
from .models import TextSummary

def summarize_text(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            summarizer = TextSummarizer()
            summary = summarizer.summarize(text)

            # Save the text and summary to the database
            TextSummary.objects.create(text=text, summary=summary)
    else:
        form = TextForm()

    # Retrieve all text-summary pairs from the database
    inputs = TextSummary.objects.all().order_by('-id')

    return render(request, 'textsummarizer/textsummarizer.html', {'form': form, 'inputs': inputs})