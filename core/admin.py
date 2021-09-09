from django.contrib import admin
from .models import Muffin


class CoreAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated' )

admin.site.register(Muffin, CoreAdmin)
