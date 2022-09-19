from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='indexpage'),
    path('staff/', views.staff, name='staffpage'),
]