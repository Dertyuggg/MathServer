
from django.shortcuts import render

def calculate_gst(request):
    if request.method == 'POST':
        try:
            price = float(request.POST.get('price', '0'))
            gst = float(request.POST.get('gst', '0'))
            total_bill = price + (price * gst / 100)
        except ValueError:
            price = 0
            gst = 0
            total_bill = 0
    else:
        price = 0
        gst = 0
        total_bill = 0
    return render(request, 'mathapp/mathapp.html', {'price': price, 'gst': gst, 'total_bill': total_bill})

    urls.py

    from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('', views.calculate_gst, name='Total')
]
