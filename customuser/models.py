from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    display_name = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )
    REQUIRED_FIELDS = ['display_name']