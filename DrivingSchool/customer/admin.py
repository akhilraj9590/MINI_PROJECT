from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomerDetails)
admin.site.register(DrivingStudyDetails)
admin.site.register(SavedLicence)
admin.site.register(ServiceApplication)
admin.site.register(schedule)
admin.site.register(Payment)
admin.site.register(balanceAndAdvance)
admin.site.register(ServiceApplicationOfRcModification)
admin.site.register(ServiceApplicationOfLicenceModification)
