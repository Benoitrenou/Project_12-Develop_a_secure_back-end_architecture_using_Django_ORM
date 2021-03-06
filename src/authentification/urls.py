from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserViewSet, MyObtainTokenPairView


router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'login/',
        MyObtainTokenPairView.as_view(),
        name='token_obtain_pair'
        ),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
