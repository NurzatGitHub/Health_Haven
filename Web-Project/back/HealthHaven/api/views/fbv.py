from django.http import JsonResponse
from rest_framework.decorators import api_view

from api.models import Post
from api.serializers import PostSerializer


@api_view(['GET'])
def post_list(request):
    if request.method == 'GET':
        categories = Post.objects.all()
        serializer = PostSerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def post_detail(request, pk=None):
    try:
        category = Post.objects.get(id=pk)
    except Post.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=400)

    if request.method == 'GET':
        serializer = PostSerializer(category)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT':
        serializer = PostSerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return JsonResponse({"deleted": True})


@api_view(['GET'])
def user_posts(request, pk=None):
    try:
        category = Post.objects.get(id=pk)
    except Post.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=400)

    serializer = PostSerializer(category)
    return JsonResponse(serializer.data)


@api_view(['GET'])
def user_data_view(request):
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({"error": "Authentication credentials were not provided."}, status=401)

    user_data = {
        'username': user.username,
        'email': user.email,
        'last_name': user.last_name

        # Add more fields as needed
    }

    if hasattr(user, 'profile'):
        user_data['phone_number'] = user.profile.phone_number
        user_data['date_of_birth'] = user.profile.date_of_birth
        
    return JsonResponse(user_data)
