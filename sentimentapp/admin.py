from django.contrib import admin
from .models import EmotionAnalysis


# Register your models here.

@admin.register(EmotionAnalysis)
class EmotionAnalysisAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'user', 'emotion']
    search_fields = ['text']

