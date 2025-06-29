from django.contrib import admin

from .models import Company, CustomUser

admin.site.register(CustomUser)
admin.site.register(Company)
