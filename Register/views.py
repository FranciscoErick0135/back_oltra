from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, UserSerializer

#Register API
class RegisterAPI(ObtainAuthToken): 
    serializer_class = RegisterSerializer 
    
    def post(self, request, *args, **kwargs): 
        serializer = self.get_serializer(data=request.data) 
        serializer.is_valid(raise_exception=True) 
        user = serializer.save() 
        token = Token.objects.create(user=user) 
        return Response({ "user": UserSerializer(user, context=self.get_serializer_context()).data, "token": token.key, })