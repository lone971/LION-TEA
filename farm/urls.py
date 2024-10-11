# farm/urls.py

from django.urls import path
from .views import FarmCreateView, FarmListView

urlpatterns = [
    path('create-farm/', FarmCreateView.as_view(), name='create_farm'),  # Endpoint to create a new farm
    path('user-farms/<str:user_email>/', FarmListView.as_view(), name='user_farms'),  # Endpoint to list farms by user email
]
