from django.urls import include, path
from rest_framework import routers
from . import views
from .views import UserViewSet, ScheduleViewSet, BlockViewSet, GoalViewSet

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'schedule', views.ScheduleViewSet)
router.register(r'block', views.BlockViewSet)
router.register(r'goal', views.GoalViewSet)

urlpatterns = [
    path('', include(router.urls), name='index'),
    # path('user/', UserViewSet.as_view({"get": "list", "post": "create"}), name='users'),
    # path('user/<int:userId>/', UserViewSet.as_view({"get": "list"}), name='getUser'),
    # path('schedule/<int:userId>/<int:scheduleId>/', views.getSchedule, name='getSchedule'),
]
