from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'topics', views.TopicViewSet)
router.register(r'lessons', views.LessonViewSet)

urlpatterns = router.urls
