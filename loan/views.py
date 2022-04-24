from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import Loan
from .serializers import LoanSerializer, LoanListSerializer

# Create your views here.


class LoanList(ListCreateAPIView):
    serializer_class = LoanListSerializer
    permission_class = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Loan.objects.filter(owner=self.request.user)



class LoanDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = LoanSerializer
    permission_class = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Loan.objects.filter(owner=self.request.user)