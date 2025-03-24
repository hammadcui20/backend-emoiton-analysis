from rest_framework import serializers
from .models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']


from rest_framework import serializers
from .models import ReportIssue


class ReportIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportIssue
        fields = ['id', 'title', 'description', 'status', 'created_at']
        read_only_fields = ['id', 'created_at']  # Prevent users from modifying these fields
