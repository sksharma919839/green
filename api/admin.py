from django.contrib import admin
from .models import *


class serviceAdmin(admin.ModelAdmin):
    list_display = ("id", "img", "h4", "p", "link")


admin.site.register(service, serviceAdmin)
