from dataclasses import fields
from rest_framework import serializers
from .models import User, Roaster, Bean


class UserSerializer(serializers.HyperlinkedModelSerializer):
    roaster = serializers.HyperlinkedRelatedField(
        view_name='roaster_detail',
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'user', 'name', 'category', 'email', 'prodile_pic',)


class RoasterSerializer(serializers.HyperlinkedModelSerializer):
    beans = serializers.HyperlinkedRelatedField(
        view_name='bean_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Roaster
        fields = ('id', 'user', 'name', 'state', 'site_url', 'display_pic')


class BeanSerializer(serializers.HyperlinkedModelSerializer):
    roaster = serializers.HyperlinkedRelatedField(
        view_name='roaster_detail',
        read_only=True
    )

    class Meta:
        model = Bean
        fields = ('id', 'roaster', 'name', 'origin', 'roast_type',
                  'description', 'price', 'buy_url', 'product_pic')
