from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import EmotionAnalysis
from .serializers import EmotionAnalysisSerializer


class EmotionAnalysisView(ListCreateAPIView):
    serializer_class = EmotionAnalysisSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Return only the current user's emotion analysis"""
        return EmotionAnalysis.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Save emotion analysis with detected sentiment"""
        serializer.save(user=self.request.user)