from django.urls import path, include
from api.views import PersonalListApiView, PersonalDetailAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.cbv import SignupAPIView
from api.views.fbv import post_list,post_detail,user_data_view


urlpatterns = [
    path('signup/', SignupAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('user_data/',user_data_view),
    path("personaldataset/", PersonalListApiView.as_view()),
    path("personaldataset/<int:id>/", PersonalDetailAPIView.as_view()),

    path('posts/',post_list),
    # path('posts/<int:pk>/',post_detail),
    # path('user/<int:pk>/posts/',User_posts)
]

