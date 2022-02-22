from django.urls import include, path
from rest_framework.routers import DefaultRouter
from clients import views

router = DefaultRouter()
router.register('companies', views.CompanyViewSet)
router.register('contacts', views.ContactViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
