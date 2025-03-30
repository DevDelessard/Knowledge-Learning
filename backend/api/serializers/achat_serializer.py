from rest_framework import serializers
from ..models.achat import Achat

class AchatSerializer(serializers.ModelSerializer):
    course_title = serializers.SerializerMethodField()
    lesson_title = serializers.SerializerMethodField()
    course_price = serializers.SerializerMethodField()
    lesson_price = serializers.SerializerMethodField()
    course_id = serializers.SerializerMethodField()
    lesson_id = serializers.SerializerMethodField()

    class Meta:
        model = Achat
        fields = [
            'id', 'type_achat', 'course', 'lesson', 'date_achat',
            'course_title', 'lesson_title', 'course_price', 'lesson_price',
            'course_id', 'lesson_id'
        ]
        read_only_fields = ['utilisateur']

    def create(self, validated_data):
        validated_data['utilisateur'] = self.context['request'].user
        return super().create(validated_data)

    def get_course_title(self, obj):
        return obj.course.title if obj.course else None

    def get_lesson_title(self, obj):
        return obj.lesson.title if obj.lesson else None

    def get_course_price(self, obj):
        return obj.course.price if obj.course else None

    def get_lesson_price(self, obj):
        return obj.lesson.price if obj.lesson else None

    def get_course_id(self, obj):
        return obj.course.id if obj.course else None

    def get_lesson_id(self, obj):
        return obj.lesson.id if obj.lesson else None

