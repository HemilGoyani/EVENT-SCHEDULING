from django.urls import path
from .views import (
    CheckAvailabilityAPIView,
    CalendarViewSet,
    DeleteMeetingAPIView,
    UpdateMeetingAPIView,
)
from rest_framework.routers import DefaultRouter

# Create a router and register the CalendarViewSet
router = DefaultRouter()
router.register('', CalendarViewSet, basename='calendar')

urlpatterns = [
    path('check-availability/', CheckAvailabilityAPIView.as_view(), name='check-availability'),
    path('delete-meeting/<int:pk>/', DeleteMeetingAPIView.as_view(), name='delete-meeting'),
    path('update-meeting/<int:pk>/', UpdateMeetingAPIView.as_view(), name='update-meeting'),
]

# Include the router's URLs
urlpatterns += router.urls
