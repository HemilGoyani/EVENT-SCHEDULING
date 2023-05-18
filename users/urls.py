from django.urls import path, include

urlpatterns = [
    # Other URL patterns...
    path('api/', include('users.urls')),
]
