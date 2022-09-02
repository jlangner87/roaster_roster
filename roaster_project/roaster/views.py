from roaster.models import Roaster
from .models import User, Roaster, Bean
from rest_framework import generics
from .serializers import UserSerializer, RoasterSerializer, BeanSerializer

# Create your views here.
# USER


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ROASTER


class RoasterList(generics.ListCreateAPIView):
    queryset = Roaster.objects.all()
    serializer_class = RoasterSerializer


class RoasterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roaster.objects.all()
    serializer_class = RoasterSerializer

# BEAN


class BeanList(generics.ListCreateAPIView):
    queryset = Bean.objects.all()
    serializer_class = BeanSerializer


class BeanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bean.objects.all()
    serializer_class = BeanSerializer
