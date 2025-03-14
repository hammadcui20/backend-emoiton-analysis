from django.apps import AppConfig
import nltk

class SentimentappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sentimentapp'

    def ready(self):
        nltk.download('vader_lexicon')
