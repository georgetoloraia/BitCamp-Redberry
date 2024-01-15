from rest_framework import serializers
from .models import Blog
import re
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['image', 'title', 'description', 'author', 'publication_date', 'categories', 'email']

    def validate_image(self, value):
        if not value:
            raise serializers.ValidationError("This field is mandatory.")
        return value

    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Title must be at least 2 characters.")
        return value

    def validate_description(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Description must be at least 2 characters.")
        return value

    def validate_author(self, value):
        if len(value.split()) < 2 or not all(char.isalpha() or char.isspace() for char in value):
            raise serializers.ValidationError("Author must be at least two words and only contain Georgian symbols.")
        return value

    def validate_categories(self, value):
        if not value:
            raise serializers.ValidationError("This field is mandatory.")
        # tu sxva validaciebi damchirda chavamateb
        return value

    def validate_email(self, value):
        if value and not value.endswith('@redberry.ge'):
            raise serializers.ValidationError("Email must end with @redberry.ge.")
        return value


class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ('email', 'password')  # Add other fields as needed
        extra_kwargs = {'password': {'write_only': False}}

    def create(self, validated_data):
        user = User.objects.create_user(email=validated_data['email'], password=None)
        return user