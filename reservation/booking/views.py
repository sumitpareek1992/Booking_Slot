from django.shortcuts import render
from booking.forms import SalonForm, TimeForm, SlotForm
# Create your views here.

def salon_view(request):
    if request.method == 'POST':
        form = SalonForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SalonForm()
    return render(request, 'salon.html',{'form': form)

def time_view(request):
    if request.method == 'POST':
        form = TimeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TimeForm()
    return render(request, 'time.html',{'form': form)

def slot_view(request):
    if request.method == 'POST':
        form = SlotForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SalonForm()
    return render(request, 'salon.html',{'form': form)