from dataclasses import fields
from rest_framework import serializers
from .models import User, Roaster, Bean


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'category', 'email', 'profile_pic',)
        depth = 1


class RoasterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roaster
        fields = ('id', 'name', 'bio', 'state',
                  'site_url', 'display_pic', 'beans_list')
        depth = 1


class BeanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bean
        fields = ('id', 'roaster', 'name', 'origin', 'bean_type', 'roast_type',
                  'description', 'organic', 'price', 'buy_url', 'product_pic')
        depth = 2
