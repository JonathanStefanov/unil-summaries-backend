from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet, CourseViewSet, SummaryViewSet, UserViewSet, UserRegistrationView, VoteView
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'faculties', FacultyViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'summaries', SummaryViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('vote/', VoteView.as_view(), name='vote'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
