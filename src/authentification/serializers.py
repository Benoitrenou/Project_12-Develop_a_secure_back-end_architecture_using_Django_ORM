from rest_framework.serializers import ModelSerializer, ValidationError,\
    CharField
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer to obtain token via JWT
    """

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token


class UserSerializer(ModelSerializer):

    password = CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
        )
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'role',
            'email',
            'phone',
            'mobile',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'username': {'required': True},
        }

    def validate(self, attrs):
        """
        Integrate verification match of password fields in data validation
        """
        if attrs['password'] != attrs['password2']:
            raise ValidationError(
                {"password": "Password fields didn't match."}
                )

        return attrs

    def create(self, validated_data):
        """
        Setup User instanciation
        """
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
