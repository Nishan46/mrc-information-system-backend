from asyncio.windows_events import NULL
from dataclasses import dataclass
import json
from unicodedata import category

from django.urls import is_valid_path
from information_system.settings import API_KEY
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .Serializers import *

# Create your views here.
@api_view(['POST'])
def Index(request):
    return Response({'message':'wada wada bn'})


@api_view(['POST','GET'])
def MEMBER_DETAILS_REGISTER(request,api_key):
    if (request.method == 'POST'):
            if API_KEY == api_key:


                member_serializer = MemberSerializer(data=json.loads(json.dumps(request.data))['body-data']['member-data'])
                if member_serializer.is_valid():
                    member_serializer.save()
                    main_json = json.loads(json.dumps(request.data))['body-data']['category-data']
                    main_json["member"] = Member.objects.get(pk=member_serializer.data['user_name'])
                    category_serializer = CategorySerializer(data = main_json)
                    if category_serializer.is_valid():
                        category_serializer.save()
                        return Response(f'success',status=status.HTTP_202_ACCEPTED)
                    else:
                        return Response('internal server error',status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    return Response('user already registered',status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                return Response("API_KEY ERROR",status=status.HTTP_502_BAD_GATEWAY)
        
            