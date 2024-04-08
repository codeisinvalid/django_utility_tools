from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import io
import json
# Create your views here.
def image_resizer(request):

    return render(request, 'imageresizer/imageresizer.html')

@csrf_exempt
def image_editor(request):
    if request.method == 'GET':
        # Render the template for the initial page load
        return render(request, 'imageresizer/imageresize_interface.html')
    elif request.method == 'POST':
        try:
            # Get the crop data from the request body
            crop_data = json.loads(request.body)
            # print(crop_data)
            x = crop_data['x']
            y = crop_data['y']
            height = crop_data['height']
            width = crop_data['width']
            scaleX = crop_data['scaleX']
            scaleY = crop_data['scaleY']
            rotate = crop_data['rotate']
           
            

            # Process the crop data as needed
            # ...

            # Return a success response
            return JsonResponse({'success': True, 'message': 'Crop data received successfully.'})
        except Exception as e:
            # Return an error response
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    else:
        # Return a method not allowed response
        return JsonResponse({'success': False, 'message': 'Method not allowed.'}, status=405)