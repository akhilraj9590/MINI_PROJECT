from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.index,name="staff-index"),
    path('appliedServices/',views.AppliedServices,name='staff-appliedServices'),
    path('studentDetails/view/<int:pk>',views.student_view,name="staff-student_view"),
    path('studentDetails/view/<int:pk>/render_pdf_view',views.render_pdf_view,name="staff-render_pdf_view"),
    path('studentDetails/',views.studentDetails,name="staff-studentsDetails"),
    path('manageAppliedServices/',views.ManageAppliedServices,name='staff-ManageAppliedServices'),
    path('update_services/<int:pk>',views.update_services,name='staff-update_services'),
    path('viewDocuments/<int:pk>',views.viewDocuments,name='staff-viewDocuments'),
    path('manageStudentSchedule',views.manageStudentSchedule,name='staff-manageStudentSchedule'),
    path('recipts',views.recipts,name='staff-recipts'),
    path('createUser',views.userRegister,name = 'staff-userRegister'),
    path('userRegisterd',views.userRegistered,name= 'staff-userRegistered'),
    path('updateLearningTestDates/<int:pk>',views.updateLearningTestDates,name="staff-updateLearningTestDates"),
    path('manageAppliedRcServices',views.ManageAppliedRCServices,name='staff-ManageAppliedRCServices'),
    path('updateRCservices/<int:pk>',views.updateRCModificationservices,name='staff-updateRCservices'),
    path('manageAppliedLicenceServices',views.ManageAppliedLicenceServices,name='staff-ManageAppliedLicenceServices'),
    path('updateLicenceservices/<int:pk>',views.updateLicenceModificationservices,name='staff-updateLicenceservices'),
    

]
