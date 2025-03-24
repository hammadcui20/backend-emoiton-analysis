from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactUs
from .serializers import ContactUsSerializer
from rest_framework.permissions import AllowAny


class ContactUsView(CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [AllowAny]  # Anyone can submit a contact message

    def create(self, request, *args, **kwargs):
        """Custom handling of contact form submission"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Your message has been submitted successfully!"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import ReportIssue
from .serializers import ReportIssueSerializer
from rest_framework.permissions import AllowAny


class ReportIssueView(ListCreateAPIView):
    queryset = ReportIssue.objects.all()
    serializer_class = ReportIssueSerializer
    permission_classes = [AllowAny]  # Allow public access

    def create(self, request, *args, **kwargs):
        """Custom create method to handle issue submission"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Issue reported successfully!"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
