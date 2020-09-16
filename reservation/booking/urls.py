from django.urls import path
from booking import views

app_name = 'booking'

urlpatterns = [
    path('salon/', views.salon_view, name='salon'),
    path('time/', views.time_view, name='time'),
    path('slot/', views.slot_view, name='slot'),
]