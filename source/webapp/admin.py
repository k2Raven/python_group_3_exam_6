from django.contrib import admin
from webapp.models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'status', 'created_at', 'updated_at']


admin.site.register(Record, RecordAdmin)

