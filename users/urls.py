from django.urls import path
from .views import some_view

urlpatterns = [
    path('some-path/', some_view, name='some-view'),
    # Add more paths as needed
]
