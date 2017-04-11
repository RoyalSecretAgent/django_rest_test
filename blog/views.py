from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework import serializers, mixins

from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class blog_api(GenericAPIView, mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args , **kwargs)

    def post(self, request, *args, **kwargs):
        return  self.create(request, *args , **kwargs)