from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import (Animal)
from .serializers import AnimalSerializer


class AnimalView(APIView):
    

    def get(self,request):
        queryset=Animal.objects.all()
        serializer=AnimalSerializer (queryset, many=True)
        return Response({
            'status':'True',
            'message':'animals fetched with get',
            'data':serializer.data
        })

    def post(self,request):
        return Response({
            'status':'True',
            'message':'animals fetched with post'
        })

    def put(self,request):
        return Response({
            'status':'True',
            'message':'animals fetched with put'
        })

    def patch(self,request):
        return Response({
            'status':'True',
            'message':'animals fetched with patch'
        })
# Create your views here.
