from django.urls import path,include
from . import views


urlpatterns = [
    path('owner/index/',views.index,name="owner-index"),
]