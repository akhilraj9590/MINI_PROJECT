from django.contrib import admin
from .models import Profile , Branch ,ServicesNameAndPrice,studyLicenceNameAndPrice


# Register your models here.
admin.site.register(Profile)
admin.site.register(Branch)
admin.site.register(ServicesNameAndPrice)
admin.site.register(studyLicenceNameAndPrice)

admin.site.site_header = 'Driving School'
