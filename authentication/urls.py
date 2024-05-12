from django.urls import path
from rest_framework import authtoken
from .views import CustomAuthToken
from .import views


urlpatterns = [
    # By exposing this built-in endpoint you will get a token
    path('api-token-auth/', authtoken.views.obtain_auth_token),
    path('custom-token-auth/', CustomAuthToken.as_view()),
    path("api/user/signup/", views.SignupAPIView.as_view(), name="user-signup"),
    path("api/user/login/", views.LoginAPIView.as_view(), name="user-login"),
    # path("api/chat/", views.ChatAPIView.as_view(), name="api-chat"),
    
]