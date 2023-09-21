from rest_framework import serializers
from django.contrib.auth.models import User

def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('admin cannot be in email!')  
    


class UserRegisterSerializer(serializers.ModelSerializer):

    password2 =serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'email' : {'validators': [clean_email]}
        }
        # excludes = ()

    def create(self, validated_data): # get argument from UserRegister from views.py
        del validated_data['password2']
        return User.objects.create_user(**validated_data)
    
    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('username cannot be admin!')
        return value

# class UserRegisterSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     email = serializers.EmailField(required=True, validators=[clean_email])
#     password = serializers.CharField(required=True, write_only=True)
#     password2 = serializers.CharField(required=True, write_only=True)

    # def validate_username(self, value):
    #     if value == 'admin':
    #         raise serializers.ValidationError('username cannot be admin!')
    #     return value
    
    # def validate(self, data):
    #     if data['password'] != data['password2']:
    #         raise serializers.ValidationError('password must be match!')
    #     return data
    

class UserSeializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'