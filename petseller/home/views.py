from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import (Animal)
from .serializers import AnimalSerializer, RegisterSerializer
from django.db.models import Q

class AnimalDetailsView(APIView):
    def get(self,request,pk):
        try:
            queryset=Animal.objects.get(pk=pk)
            queryset.incrementViews()
            serializer =AnimalSerializer(queryset)
            return Response({
                  'status':True,
                    'message':'animals fetched with get',
                    'data':serializer.data
            })
        except Exception as e:
            print(e)
            return Response({
                  'status':False,
                    'message':'animals fetched with get',
                    'data':{}
            })




class AnimalView(APIView):
    def get(self,request):
        queryset=Animal.objects.all() 

        if request.GET.get('search'):
            search=request.GET.get('search')
            queryset = queryset.filter(
                Q(animal_name__icontains =search) |
                Q(animal_description__icontains =search) |
                Q(animal_gender__iexact =search) |
                Q(animal_breed__animal_breed__icontains =search) |
                Q(animal_color__animal_color__icontains =search) 
                )

        serializer=AnimalSerializer (queryset, many=True)
        return Response({
            'status':True,
            'message':'animals fetched with get',
            'data':serializer.data
        })

    def post(self,request):
        return Response({
            'status':True,
            'message':'animals fetched with post'
        })

    def put(self,request):
        return Response({
            'status':True,
            'message':'animals fetched with put'
        })

    def patch(self,request):
        return Response({
            'status':True,
            'message':'animals fetched with patch'
        })


class RegisterAPI(APIView):
    def post(self,request):
        try:
            data =request.data
            serializer= RegisterSerializer(data=data)
            if serializer.is_valid():
                return Response({
                    'status':True,
                    'message':'account created',
                    'data':{}
                })
            
            return Response({
                'status':False,
                'message':'keys error',
                'data':serializer.error()
            })

        except Exception as e:
            print(e)
# Create your views here.
