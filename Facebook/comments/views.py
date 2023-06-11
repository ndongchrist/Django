from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Comment
from .serializer import CommentSerializer

# Create your views here.
def hello(request):
    return HttpResponse("<marquee>Hello This is wendy</marquee>")

@api_view(['GET'])
def get(request):
    data = Comment.objects.all()
    serializer = CommentSerializer(data, many=True)
    return Response(serializer.data)
    
@api_view((['POST']))
def add(request):
    data = request.data
    cmt = Comment.objects.create(
        text = data['text'],
        username = data['username'],
        time = data['time']
    )
    serializer = CommentSerializer(cmt)
    return Response(serializer.data)
