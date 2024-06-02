from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny

from ..models import PersonalData
from ..serializers import PersonalDataSerializer2

class PersonalListApiView(generics.ListCreateAPIView):
    serializer_class = PersonalDataSerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return PersonalData.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PersonalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalData.objects.all()
    serializer_class = PersonalDataSerializer2
    permission_classes = (IsAuthenticated,)
