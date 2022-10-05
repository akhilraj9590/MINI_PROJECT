from django.urls import path,include
from . import views


urlpatterns = [
    path('customer/index/',views.index,name="customer-index"),
]