from rest_framework import serializers
from .models import Answer, Question

class PersonSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField() # if we don't use from this line in just dose not show
    # 

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        field = '__all__'