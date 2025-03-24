from django.urls import path
from .views import ContactUsView, ReportIssueView

urlpatterns = [
    path('contact/', ContactUsView.as_view(), name='contact-us'),
    path('report-issue/', ReportIssueView.as_view(), name='report-issue'),
]
