from django.urls import include, path
from rest_framework.routers import DefaultRouter
from events import views


router = DefaultRouter()
router.register('events', views.EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
