from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

        def create(self, validated_data):
            model = self.Meta.model
            posts = model.objects.create(**validated_data)
            posts.save()
            return posts