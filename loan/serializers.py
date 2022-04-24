from rest_framework.serializers import ModelSerializer
from .models import Loan


class LoanSerializer(ModelSerializer):

    class Meta:
        model=Loan

        fields=['id', 'start_date', 'end_date', 'book_id', 'created_date', 'updated_date']


class LoanListSerializer(ModelSerializer):
    
    class Meta:
        model=Loan

        fields=['id', 'start_date', 'end_date', 'book_id', 'created_date', 'updated_date', 'owner']
