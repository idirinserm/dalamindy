from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgrammeViewSet, CourseViewSet, VideoViewSet, TextViewSet

router = DefaultRouter()
router.register(r'programmes', ProgrammeViewSet, basename='programme')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'videos', VideoViewSet, basename='video')
router.register(r'texts', TextViewSet, basename='text')

urlpatterns = [
    path('', include(router.urls)),
]