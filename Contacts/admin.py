from django.contrib import admin
from .models import People
# Register your models here.


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone']


admin.site.register(People, PhoneAdmin)