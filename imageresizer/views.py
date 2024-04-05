from django.shortcuts import render

# Create your views here.
def image_resizer(request):
    return render(request, 'imageresizer/imageresizer.html')
