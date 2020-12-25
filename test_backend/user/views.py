from user.models import User
from user.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password


# Create your views here.
class RegisterView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        request.data["password"]=make_password(request.data["password"])
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User Created Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        user = authenticate(request, username=request.data["username"], password=request.data["password"])

        if user is not None:
            login(request, user)
            return Response({"message": "Login Successfull"}, status=status.HTTP_200_OK)

        else:
            return Response({"message": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

    def get(self,request):
        logout(request)
        return Response({"message": "Logout Successfull"}, status=status.HTTP_200_OK)
