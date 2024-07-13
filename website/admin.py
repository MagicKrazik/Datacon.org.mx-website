from django.contrib import admin
from .models import QuoteRequest, ContactMessage

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'project_type', 'created_at')
    list_filter = ('project_type', 'budget', 'created_at')
    search_fields = ('name', 'email', 'company', 'project_description')
    readonly_fields = ('created_at',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)


    