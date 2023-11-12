from rest_framework import serializers
from .models import Programme, Course, Video, Text

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'video_url']

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ['id', 'title', 'content']

class CourseSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    texts = TextSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'videos', 'texts']

class ProgrammeSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Programme
        fields = ['id', 'title', 'description', 'courses']
