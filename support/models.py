from django.db import models


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


STATUS_CHOICES = (
    ('Open', 'Open'),
    ('In Progress', 'In Progress'),
    ('Resolved', 'Resolved')
)


class ReportIssue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()  # Changed from EmailField to TextField
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
