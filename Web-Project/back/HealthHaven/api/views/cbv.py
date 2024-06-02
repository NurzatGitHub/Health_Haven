from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
    
class SignupAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        email = request.data.get('email')
        # phone_number = request.data.get('phone_number')
        # date_of_birth = request.data.get('date_of_birth')

        if not (username and password):
            return Response({'error': 'Both username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, 
                                        last_name=last_name, 
                                        email=email, 
                                        password=password
                                        )

        if user:
            return Response({'success': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Failed to create user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


from ..models import PersonalData
from ..serializers import PersonalDataSerializer2,PersonalDataSerializer

class PersonalListApiView(APIView):
    def get(self, request):
        PersonalDataset = PersonalData.objects.all()
        serializer = PersonalDataSerializer2(PersonalDataset,many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = PersonalDataSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonalDetailAPIView(APIView):
    def get_object(self, id):
        try:
            perData = PersonalData.objects.get(id = id)
            return perData
        except PersonalData.DoesNotExist as e:
            return None
        
    def get(self, request, id):
        perData = self.get_object(id)

        if perData is None:
            return Response({"error": "PersonalData not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonalDataSerializer(perData)
        return Response(serializer.data)
    
    def put(self, request, id):
        perData = self.get_object(id)

        if perData is None:
            return Response({"error": "PersonalData not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonalDataSerializer(instance=perData, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        perData = self.get_object(id)

        if perData is None:
            return Response({"error": "PersonalData not found"}, status=status.HTTP_404_NOT_FOUND)
        
        perData.delete()
        return Response({"deleted": True})