from django.contrib import admin
from .models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file',)
    search_fields = ('title',)

admin.site.register(File, FileAdmin)
