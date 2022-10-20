from django.urls import path,include
from . import views


urlpatterns = [
    path('index/',views.index,name="owner-index"),
    path('staffDetails/',views.staffDetails,name="owner-staffDetails"),
    path('studentDetails/',views.studentDetails,name="owner-studentDetails"),
    path('instructor/',views.instructor,name="owner-instructor"),
    path('appliedServices/',views.appliedServices,name="owner-appliedServices"),
]