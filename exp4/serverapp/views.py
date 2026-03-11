from django.shortcuts import render

def bill(request):
    total = None

    if request.method == "POST":
        price = float(request.POST.get("price"))
        gst = float(request.POST.get("gst"))

        total = price + (price * gst / 100)

    return render(request, "bill.html", {"total": total})