# 序列化
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from yy import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class YYUserSerializer(serializers.HyperlinkedModelSerializer):
    # username = serializers.CharField()

    class Meta:
        model = models.User
        fields = "__all__"
