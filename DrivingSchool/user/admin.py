from django.contrib import admin
from .models import Profile , Branch ,ServicesNameAndPrice


# Register your models here.
admin.site.register(Profile)
admin.site.register(Branch)
admin.site.register(ServicesNameAndPrice)

admin.site.site_header = 'Driving School'
