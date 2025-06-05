from django.shortcuts import render
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings

def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            rest_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']

            # Generate QR Code
            qr = qrcode.make(url)
            file_name = rest_name.replace(" ","_").lower() + '_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name) # media/rathan_rest_menu.png
            qr.save(file_path)

            print('file_path==>', file_path )
            # Create IMAGE URL
            qr_url = os.path.join(settings.MEDIA_URL, file_name)
           

            context ={
                'rest_name': rest_name,
                'qr_url': qr_url,
                'file_name' : file_name,
            }
            return render(request,'qr_result.html', context)

            
    else:
        form = QRCodeForm()
        context = {
            'form': form,
        }
        return render(request, 'generate_qr_code.html', context)