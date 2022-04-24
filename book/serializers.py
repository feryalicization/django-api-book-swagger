from rest_framework.serializers import ModelSerializer
from .models import Book


class BookSerializer(ModelSerializer):

    class Meta:
        model=Book

        fields=['id', 'book_name', 'photo', 'is_loan', 'created_date', 'updated_date']

