from django.shortcuts import render

from rest_framework import viewsets

from .models import Category

from .serializers import CategorySerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    model = Category
    serializer_class = CategorySerializer

    #paginate_by = 1
    #filter_fields = ('name')