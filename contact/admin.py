# contact/admin.py (修正案)

from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'inquiry_type', 'contact_method', 'created_at', 'replied')
    list_filter = ('replied', 'inquiry_type', 'contact_method', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'created_at'

    # 編集可能なフィールド
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone', 'subject', 'inquiry_type', 'contact_method', 'message')
        }),
        ('返信情報', {
            'fields': ('replied', 'reply_message', 'replied_at'),
            'classes': ('collapse',), # 返信情報を折りたたんで表示
        }),
    )