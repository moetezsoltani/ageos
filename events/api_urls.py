from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import EventViewSet, PublicationViewSet, FormationViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'publications', PublicationViewSet)
router.register(r'formation', FormationViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
