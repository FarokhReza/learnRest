from rest_framework import serializers
from .models import Answer, Question
from .custome_relational_fields import UserEmailNameRelationalFields

class PersonSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField() # if we don't use from this line in just dose not show
    # 

class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    user = UserEmailNameRelationalFields(read_only=True)
    # user = serializers.StringRelatedField(read_only=True)
    # user = serializers.SlugRelatedField(read_only=True, slug_field='email')
    # user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

    def get_answers(self, obj):

        result = obj.answers.all()
        return AnswerSerializer(instance=result, many=True).data

    


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'