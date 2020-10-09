from rest_framework import serializers
from django.conf import settings
from .models import Tweets

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = ['content']

    def validate_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError("This tweet is too long")
        return value
