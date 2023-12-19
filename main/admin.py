from django.contrib import admin

from .models import post
# Register your models here.

class postAdmin(admin.ModelAdmin):
    
    list_display=("titulo", "description", "created", "updated")

    # Establece los campos 'created' y 'updated' como campos de solo lectura en la interfaz de administración
    readonly_fields = ('created', 'updated')
    
admin.site.register(post, postAdmin)