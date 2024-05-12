from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import SignupSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token




class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
        })



class SignupAPIView(APIView):
    def post(self,request):
        serializer = SignupSerializer(data = request.data)
        if serializer.is_valid():
                serializer.save()
                print(serializer)

                res = { 'status' : status.HTTP_201_CREATED }
                return Response(res, status = status.HTTP_201_CREATED)
        res = { 'status' : status.HTTP_400_BAD_REQUEST, 'data' : serializer.errors }
        return Response(res, status = status.HTTP_400_BAD_REQUEST)




class LoginAPIView(APIView):
    def post(self,request):
            serializer = LoginSerializer(data = request.data)
            if serializer.is_valid():
                    username = serializer.validated_data["username"]
                    password = serializer.validated_data["password"]
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        token = Token.objects.get(user=user)
                        response = {
                               "status": status.HTTP_200_OK,
                               "message": "success",
                               "data": {
                                    "Token" : token.key
                               }
                               }
                        return Response(response, status = status.HTTP_200_OK)
                    else :
                        response = {
                               "status": status.HTTP_401_UNAUTHORIZED,
                               "message": "Invalid Username or Password",
                               }
                        return Response(response, status = status.HTTP_401_UNAUTHORIZED)
            response = {
                 "status": status.HTTP_400_BAD_REQUEST,
                 "message": "bad request",
                 "data": serializer.errors
                 }
            return Response(response, status = status.HTTP_400_BAD_REQUEST)



