from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MyModel


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user






class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__' # Or specify a list of fields

    # def create(self, validated_data):
    # user = User.objects.create_user(
    #     username=validated_data['username'],
    #     password=validated_data['password']
    # )
    # return user