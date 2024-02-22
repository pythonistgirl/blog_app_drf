from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        data = request.data
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class RetrivePostsView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        list = PostSerializer.objects.all()
        serializer = PostSerializer(list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)