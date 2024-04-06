from django.shortcuts import render

# Create your views here.
def image_resizer(request):

    return render(request, 'imageresizer/imageresizer.html')

def image_editor(request):
    # img_src = request.GET.get('image','')
    return render(request, 'imageresizer/imageresize_interface.html')

