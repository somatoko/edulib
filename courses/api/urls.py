from django.urls import include, path
from rest_framework import routers
from . import views


app_name = 'courses'


router = routers.DefaultRouter()
router.register('subjects', views.SubjectViewSet)
router.register('courses', views.CourseViewSet)


urlpatterns = [
    # path('courses/<pk>/enroll/', views.CourseEnrollView.as_view(), name='course_enroll'),
    path('', include(router.urls)),
]