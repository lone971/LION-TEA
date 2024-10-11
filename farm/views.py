# farm/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Farm
from .serializers import FarmSerializer

class FarmCreateView(generics.CreateAPIView):
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FarmListView(generics.ListAPIView):
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_email = self.kwargs['user_email']
        return Farm.objects.filter(user__email=user_email)
