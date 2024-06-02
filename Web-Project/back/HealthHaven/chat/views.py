from django.shortcuts import render
from .pusher import pusher_client  
from rest_framework.response import Response

# Create your views here.

from rest_framework.views import APIView

class MessageAPIView(APIView):
    
    def post(self, request):
        pusher_client.trigger('my_channel','my_event',{
            'username': request.data['username'],
            'message': request.data['message'],
            })
        
        return Response('sended')