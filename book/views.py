from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer
from rest_framework import permissions
from .models import Book

# Create your views here.


class BookList(ListCreateAPIView):
    serializer_class = BookSerializer
    permission_class = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)


class BookDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_class = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)



