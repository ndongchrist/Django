from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Author, Book
from .serializer import BookSerializer, AuthorSerializer

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")