from django.urls import path,include
from . import views


urlpatterns = [
    path('index/',views.index,name="owner-index"),
    path('staffDetails/',views.staffDetails,name="owner-staffDetails"),
    path('studentDetails/',views.studentDetails,name="owner-studentDetails"),
    path('instructor/',views.instructor,name="owner-instructor"),
    path('appliedServices/',views.appliedServices,name="owner-appliedServices"),
    path('addInstructor/',views.addInstructor,name="owner-addInstructor"),
    path('addStaff/',views.addStaff,name="owner-addStaff"),
    path('addStudent/',views.addStudent,name="owner-addStudent"),
    path('recipts',views.totalRecipt,name="owner-recipt"),
    path('createUser',views.userRegister,name="owner-createUser"),
    path('userCreatedSuccesfully',views.userCreated,name='owner-userCreated')
]