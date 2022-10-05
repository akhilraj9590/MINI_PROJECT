from django.urls import path,include
from . import views


urlpatterns = [
    path('staff/index/',views.index,name="customer-index"),
    path('dashboard/',views.dashboard,name="dashbaord-index"),
]