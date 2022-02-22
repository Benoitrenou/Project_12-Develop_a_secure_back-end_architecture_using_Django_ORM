from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserSerializer,\
    MyTokenObtainPairSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class MyObtainTokenPairView(TokenObtainPairView):
    """
    View to obtain token via JWT
    """
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
