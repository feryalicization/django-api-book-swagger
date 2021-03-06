from django.db import models
from django.contrib.auth.models import User
from pytz import timezone
from django.utils.timezone import now

# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=20)
    photo = models.URLField(null=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    is_loan = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=now, blank=True)
    updated_date = models.DateTimeField(default=now, blank=True)
    deleted_date = models.DateTimeField(default=now, blank=True)


