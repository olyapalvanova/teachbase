from django.db import transaction
from rest_framework import serializers

from apps.courses.models import Course, CourseType, CourseAuthor


class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = ('id', 'name', 'created_at', 'updated_at',)


class CourseAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAuthor
        fields = (
            'id', 'email', 'phone', 'name', 'last_name', 'role_id', 'auth_type',
            'last_activity_at', 'is_active', 'created_at', 'updated_at',
        )


class CourseSerializer(serializers.ModelSerializer):
    types = CourseTypeSerializer(many=True)
    authors = CourseAuthorSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            'id', 'name', 'created_at', 'updated_at', 'owner_id', 'owner_name',
            'thumb_url', 'cover_url', 'description', 'last_activity',
            'total_score', 'total_tasks', 'unchangeable',
            'include_weekly_report', 'content_type', 'is_netology', 'bg_url',
            'video_url', 'demo', 'custom_author_names', 'custom_contents_link',
            'hide_viewer_navigation', 'duration', 'types', 'authors',
        )

    @transaction.atomic
    def create(self, validated_data):
        types = validated_data.pop('types')
        authors = validated_data.pop('authors')

        instance = super().create(validated_data)

        # create CourseType objects
        data_types = [CourseType(
            course=instance, name=type['name']
        ) for type in types]
        CourseType.objects.bulk_create(data_types)

        # create  CourseAuthor objects
        data_authors = [CourseAuthor(
            course=instance, email=author['email'], phone=author['phone'],
            name=author['name'], last_name=author['last_name'],
            role_id=author['role_id'], auth_type=author['auth_type'],
            last_activity_at=author.get('last_activity_at'),
            is_active=author['is_active']
        ) for author in authors]
        CourseAuthor.objects.bulk_create(data_authors)

        return instance
