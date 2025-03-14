from rest_framework import serializers
from .models import EmotionAnalysis


class EmotionAnalysisSerializer(serializers.ModelSerializer):
    emotion = serializers.CharField(read_only=True)

    class Meta:
        model = EmotionAnalysis
        fields = '__all__'
