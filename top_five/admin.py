from django.contrib import admin
from .models import Query


@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp',)
    search_fields = ('title',)
    ordering = ('-timestamp',)
