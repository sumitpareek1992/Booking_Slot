from django import forms
from bookin.models import Salon, Time, Slot

class SalonForm(forms.ModelForm):
    class Meta():
        model = Salon
        fields = '__all__'

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = '__all__'

class SlotForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = '__all__'