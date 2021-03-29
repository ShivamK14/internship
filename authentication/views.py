import random
from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer, OtpSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt
from .models import UserOTP
from django.contrib.auth.models import User
from .utils import Utils

class Register(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=serializer.data['email'])
            OTP = random.randint(100000, 999999)
            UserOTP.otp = OTP  # 'http://'+current_site+relativelink+"?token="+str(token)
            email_body = 'Hi ' + user.username + ' OTP for verification is \n' + str(OTP)
            data = {'email_body': email_body,
                    'to_email': user.email,
                    'email_subject': 'verify your email',
                    }
            Utils.send_email(data)
            return Response({'user':serializer.data, 'token': 'not empty'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        print(username)
        print(password)

        if user:
            auth_token = jwt.encode({'username': user.username}, settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)


            data = {'user': serializer.data, 'token': auth_token}
            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'invalid credentials'},   status=status.HTTP_401_UNAUTHORIZED)


class VerifyOTPView(GenericAPIView):
    serializer_class = OtpSerializer
    def post(self, request):
        data = request.data
        otp = int(data.get('otp',''))
        print(UserOTP.otp)
        print(otp)
        if UserOTP.otp == otp:
            User.is_verified = True
             #user.otp.delete()  #?? How to handle the otp, Should I set it to null??
            User.save(self)
            return Response("Verification Successful")
        else:
            raise PermissionDenied({"OTP Verification failed": UserOTP.otp})



