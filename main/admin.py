from django.contrib import admin

from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    
    list_display=("titulo", "description", "created", "updated")

    # Establece los campos 'created' y 'updated' como campos de solo lectura en la interfaz de administración
    readonly_fields = ('created', 'updated')
    
admin.site.register(Post, PostAdmin)