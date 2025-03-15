from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    is_admin_user = models.BooleanField(default=False)
    is_analyst = models.BooleanField(default=True)
    dob = models.DateField(null=True, blank=True)

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return self.username
