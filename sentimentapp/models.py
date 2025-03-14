from django.db import models
from users.models import User
import nltk
from django.contrib.auth import get_user_model
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

User = get_user_model()

class EmotionAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()
    emotion = models.CharField(max_length=20)  # Example: 'Happy', 'Sad'
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Auto-detect sentiment before saving"""
        sia = SentimentIntensityAnalyzer()
        sentiment_score = sia.polarity_scores(self.text)["compound"]

        if sentiment_score >= 0.05:
            self.emotion = "Positive"
        elif sentiment_score <= -0.05:
            self.emotion = "Negative"
        else:
            self.emotion = "Neutral"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username if self.user else 'Anonymous'} - {self.emotion}"
