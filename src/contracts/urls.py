from django.urls import include, path
from rest_framework.routers import DefaultRouter
from contracts import views


router = DefaultRouter()
router.register('contracts', views.ContractViewSet)

urlpatterns = [
    path('', include(router.urls)),
]