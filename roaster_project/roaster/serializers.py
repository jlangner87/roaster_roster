from dataclasses import fields
from rest_framework import serializers
from .models import User, Roaster, Bean, Retailer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'category', 'email', 'profile_pic',)
        depth = 1


class RoasterSerializer(serializers.ModelSerializer):
    beans_list = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='name')

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


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ("id", "name", "address", "address_line2",
                  "city", "state", "zipcode")
