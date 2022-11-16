from django.urls import path,include
from . import views


urlpatterns = [
    path('index/',views.index,name="customer-index"),
    path('admission/',views.admission,name="customer-admission"),
    # path('selectBranch/',views.selectBranch,name="customer-selectBranch"),
    path('applyNewLicence/',views.applyNewLicence,name='customer-applyNewLicence'),
    path('appliedService',views.appliedService,name='customer-appliedService'),
    path('DrivingPaymentHistory',views.DrivingPaymentHistory,name='customer-DriningPaymentHistory'),
    path('schedule',views.schedules,name='customer-schedules'),
    path('attendence',views.attendence,name='customer-attendence'),
    path('pay',views.pay,name='customer-pay'),
    path('RcModification',views.RcModication,name="customer-RcModification"),
    path('appliedRcService',views.appliedRcService,name="customer-appliedRcService"),
    path('applyLicenceModificationService',views.applyLicenceModificationService,name='customer-applyLicenceModificationService'),
    path('appliedLicenceModificationService',views.appliedLicenceModificationService,name='customer-appliedLicenceModificationService'),
]