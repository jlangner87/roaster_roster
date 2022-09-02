from dataclasses import fields
from rest_framework import serializers
from .models import User, Roaster, Bean


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'category', 'email', 'profile_pic',)


class RoasterSerializer(serializers.HyperlinkedModelSerializer):
    beans = serializers.HyperlinkedIdentityField(
        view_name='bean_detail',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Roaster
        fields = ('id', 'name', 'bio', 'state',
                  'site_url', 'display_pic', 'beans')


class BeanSerializer(serializers.HyperlinkedModelSerializer):
    roaster = serializers.HyperlinkedRelatedField(
        view_name='roaster_detail',
        read_only=True
    )

    class Meta:
        model = Bean
        fields = ('id', 'roaster', 'name', 'origin', 'bean_type', 'roast_type',
                  'description', 'organic', 'price', 'buy_url', 'product_pic')
