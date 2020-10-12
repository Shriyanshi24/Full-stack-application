from rest_framework import viewsets

from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    # what is the data bringing from database
    queryset = Category.objects.all().order_by('name')
    # what is the class being responsible for serializing my data
    serializer_class = CategorySerializer
    # now query is in json format

# Create your views here.
