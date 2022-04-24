from django.db import models
from django.contrib.auth.models import User
from pytz import timezone
from django.utils.timezone import now
from book.models import Book


# Create your models here.
class Loan(models.Model):
    start_date = models.DateTimeField(default=now, blank=True)
    end_date = models.DateTimeField(blank=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now, blank=True)
    updated_date = models.DateTimeField(default=now, blank=True)
    deleted_date = models.DateTimeField(default=now, blank=True)