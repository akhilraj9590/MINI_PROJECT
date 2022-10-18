from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.index,name="staff-index"),
    path('appliedServices/',views.AppliedServices,name='staff-appliedServices'),
]