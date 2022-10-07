from django.contrib import admin
from .models import Profile , Branch


# Register your models here.
admin.site.register(Profile)
admin.site.register(Branch)

admin.site.site_header = 'Driving School'
