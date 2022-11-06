from django.urls import path,include
from . import views


urlpatterns = [
    path('index/',views.index,name="customer-index"),
    path('admission/',views.admission,name="customer-admission"),
    # path('selectBranch/',views.selectBranch,name="customer-selectBranch"),
    path('applyNewLicence/',views.applyNewLicence,name='customer-applyNewLicence'),
    path('appliedService',views.appliedService,name='customer-appliedService'),
    path('DrivingPaymentHistory',views.DrivingPaymentHistory,name='customer-DriningPaymentHistory'),
]