from django.urls import path
from .views import EmotionAnalysisView

urlpatterns = [
    path('analyze/', EmotionAnalysisView.as_view(), name='analyze'),
]
