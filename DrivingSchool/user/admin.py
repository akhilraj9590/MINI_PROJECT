from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Profile)
admin.site.register(Branch)
admin.site.register(ServicesNameAndPrice)
admin.site.register(studyLicenceNameAndPrice)
admin.site.register(Instructor)

admin.site.site_header = 'Driving School'
