from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.authentication import
    TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.pagination import
    LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND,
    HTTP_200_OK
from rest_framework.views import APIView  

from rest_framework.decorators import api_view 
  from rest_framework.response import Response 
  from .models import Course
  @api_view()
  def first_api_view(request): 
      num_books = Course.objects.count()
      return Response({"num_course": num_courses})

  from rest_framework import viewsets 
  from rest_framework.pagination import (
      LimitOffsetPagination)
  from .models import Book, Review
  from .serializers import (BookSerializer,
       ReviewSerializer)
  class BookViewSet(viewsets.ReadOnlyModelViewSet): 
      queryset = Book.objects.all() serializer_class 
      = BookSerializer
  class ReviewViewSet(viewsets.ModelViewSet): 
      queryset = Review.objects.order_by('-
      date_created')) 
          serializer_class = ReviewSerializer
      pagination_class = LimitOffsetPagination 
      authentication_classes = []