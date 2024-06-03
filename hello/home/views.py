from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PersonSerializer,RegisterSerializer,LoginSerializer
from .models import Person
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class PersonAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        obj= Person.objects.all()
        serializer= PersonSerializer(obj,many= True)
        return Response(serializer.data)
    
    def post(self, request):
        data= request.data 
        serializer= PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def patch(self,request):
        data= request.data 
        obj= Person.objects.get(id= data['id'])
        serializer= PersonSerializer(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request):
        data= request.data 
        obj= Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'Details Deleted'})
    
class RegisterApi(APIView):
    def post(self,request):
        data= request.data 
        serializer= RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response({'User Created'})
    

class LoginAPI(APIView):
    def post(self,request):
        data= request.data 
        serializer= LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        user= authenticate(username= serializer.data['username'],password= serializer.data['password'])
        if not user:
            return Response({'Invalid Credentials'})
        token ,_= Token.objects.get_or_create(user=user)
        return Response({'message':'User Logged In Successfully','token':str(token)})