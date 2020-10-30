from django.contrib import admin
from .models import *
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ['added_date','text']

#class PriceAdmin(admin.ModelAdmin):
#    list_display = ['name','price', 'slug' ,'digital']

admin.site.register(Todo ,TodoAdmin)