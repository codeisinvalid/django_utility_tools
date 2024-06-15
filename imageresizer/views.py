from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



# Create your views here.
def image_resizer(request):
    if request.method=="GET":
        return render(request, 'imageresizer/imageresizer.html')
    
    elif request.method=='POST':
        try:
            image_data = request.body
            request.session['image_data'] = image_data
            return JsonResponse({'success': True, 'message': 'Image data received successfully.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    else:
        # Return a method not allowed response
        return JsonResponse({'success': False, 'message': 'Method not allowed.'}, status=405)


@csrf_exempt
def image_editor(request):
    if request.method == 'GET':
        image_data = request.session.get('image_data', None)
        # if not image_data:
        #     return JsonResponse({'success': False, 'message': 'Image data not found in the session'}, status=400)
        print(image_data)
        # Render the template for the initial page load
        return render(request, 'imageresizer/imageresize_interface.html')
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            if 'crop' in data:
                crop_data = data['crop']
                x = crop_data['x']
                y = crop_data['y']
                height = crop_data['height']
                width = crop_data['width']
                scaleX = crop_data['scaleX']
                scaleY = crop_data['scaleY']
                rotate = crop_data['rotate']
                # Process crop data...

            if 'resize' in data:
                resize_data = data['resize']
                width = resize_data['width']
                height = resize_data['height']
                # Process resize data...

            # Return a success response
            return JsonResponse({'success': True, 'message': 'Crop data received successfully.'})
        except Exception as e:
            # Return an error response
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    else:
        # Return a method not allowed response
        return JsonResponse({'success': False, 'message': 'Method not allowed.'}, status=405)