from django.db import models
from users.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone


class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
