from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView


#-------------MODELOS-------------

from Profile.models import ProfileModel
from Profile.models import ProfilePersons

#---------------SERIALIZERS---------------

from Profile.serializers import ProfileModelSerializers
from Profile.serializers import ProfilePersonSerializer

#-----------------VIEWS-------------

class ProfileModelView(APIView):

    def post(self, request, format=None):
        serializer = ProfileModelSerializers(data = request.data, contex = {'request':request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        #response = ResponseJson("Error")
        return Response("Error Formato")

class ProfilePersonsView(APIView):

    def post(self, request, format=None):
        serializer = ProfilePersonSerializer(data = request.data, context = {'request':request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        #response = ResponseJson("Error")
        return Response("Error Formato")
    
    def put(self, request, format=None):
        profile = ProfilePersons.objects.get(id = request.data.get('id'))
        profile.nombre = request.data.get('nombre')
        profile.edad = request.data.get('edad')
        profile.correo = request.data.get('correo')
        profile.save()
        return Response('Modificado con éxito')

    def delete(self, request, format=None):
        profile = ProfilePersons.objects.get(id = request.data.get('id'))
        profile.delete()
        #response = ResponseJson("Error")
        return Response("Eliminado con éxito")
    
    def get(self, request):
        profile = ProfilePersons.objects.all()
        serializer = ProfilePersonSerializer(profile, many = True, context = {'request':request})
        #response = ResponseJson("Error")
        return Response(serializer.data)

