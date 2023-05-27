from django.contrib import admin
from .models import Jobs

class JobAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ACTIVITY iNFORMATION',{'fields':['activity']}),
        ('DESCRIPTION INFORMATION',{'fields':['description']})
    ]

admin.site.register(Jobs,JobAdmin)
# Register your models here.
