from rest_framework import serializers
from .models import Faculty, Course, Summary, Vote
from django.contrib.auth.models import User

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SummarySerializer(serializers.ModelSerializer):
    uploader_name = serializers.SerializerMethodField()
    faculty_name = serializers.SerializerMethodField()
    course_name = serializers.CharField(source='course.name', read_only=True) 

    class Meta:
        model = Summary
        fields = ['id', 'name', 'file', 'rating', 'course_name', 'uploader_name', 'faculty_name']
        read_only_fields = ['uploader']  # Make 'uploader' read-only
    
    def get_faculty_name(self, obj):
        # obj is a Summary instance. Access its course, then the faculty of that course.
        return obj.course.faculty.name
    
    def get_uploader_name(self, obj):
        # obj is a Summary instance. Access its uploader.
        return obj.uploader.username

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'faculty']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'summary', 'upvoted']
        read_only_fields = ['id']

    def create(self, validated_data):
        user = self.context['request'].user
        summary = validated_data['summary']
        upvoted = validated_data.get('upvoted', True)

        vote, created = Vote.objects.update_or_create(
            user=user, summary=summary,
            defaults={'upvoted': upvoted}
        )
        return vote