from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MyModel
from .models import Task



MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
ALLOWED_AUDIO_TYPES = ('audio/mpeg', 'audio/mp3', 'audio/wav', 'audio/x-wav', 'audio/ogg')
ALLOWED_FILE_TYPES = ('application/pdf', 'image/jpeg', 'image/png', 'text/plain', 'application/zip')

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['id', 'owner', 'text', 'audio', 'attachment', 'created_at', 'updated_at']
        read_only_fields = ['id', 'owner', 'created_at', 'updated_at']

    def validate_audio(self, file):
        if file is None:
            return file
        content_type = getattr(file, 'content_type', None)
        if content_type and content_type not in ALLOWED_AUDIO_TYPES:
            raise serializers.ValidationError("Unsupported audio type.")
        if file.size > MAX_FILE_SIZE:
            raise serializers.ValidationError("Audio file too large (max 10 MB).")
        return file

    def validate_attachment(self, file):
        if file is None:
            return file
        content_type = getattr(file, 'content_type', None)
        if content_type and content_type not in ALLOWED_FILE_TYPES:
            raise serializers.ValidationError("Unsupported attachment type.")
        if file.size > MAX_FILE_SIZE:
            raise serializers.ValidationError("Attachment file too large (max 10 MB).")
        return file

    def create(self, validated_data):
        user = self.context['request'].user
        return Task.objects.create(owner=user, **validated_data)

    def update(self, instance, validated_data):
        # default behavior is fine (DRF handles file replacement)
        return super().update(instance,validated_data)


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