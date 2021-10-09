from django.contrib import admin
from contractor.models import Profile, Employee


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile', 'business_name', 'created_at')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'phone_number', 'created_at')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Employee, EmployeeAdmin)
