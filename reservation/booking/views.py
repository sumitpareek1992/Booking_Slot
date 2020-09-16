from django.shortcuts import render, redirect
from booking.forms import SalonForm, TimeForm, SlotForm
from booking.models import Salon, Time, Slot
# Create your views here.

def salon_view(request):
    salon = Salon.objects.all()
    if request.method == 'POST':
        form = SalonForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SalonForm()
    return render(request, 'salon.html',{'form': form, 'salon':salon})

def time_view(request):
    time = Time.objects.all()
    if request.method == 'POST':
        form = TimeForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TimeForm()
    return render(request, 'time.html',{'form': form, 'time':time})

def slot_view(request):
    slot = Slot.objects.all()
    if request.method == 'POST':
        form = SlotForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SlotForm()
    return render(request, 'slot.html',{'form': form, 'slot':slot})