from django.shortcuts import render
from rest_framework import generics
from .serializers import BeanSerializer, UserSerializer, RoasterSerializer
from .models import User, Roaster, Bean
# Create your views here.


class BeanList(generics.ListCreateAPIView):
    queryset = Bean.objects.all()
    serializer_class = BeanSerializer


class BeanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bean.objects.all()
    serializer_class = BeanSerializer


class RoasterList(generics.ListCreateAPIView):
    queryset = Roaster.objects.all()
    serializer_class = RoasterSerializer


class RoasterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roaster.objects.all()
    serializer_class = RoasterSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
