
from dataclasses import Field, fields
import json
from os import stat
from information_system.settings import API_KEY
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .Serializers import *
from .models import *
from .Core import *

# Create your views here. 
@api_view(['Get'])
def Index(request):
    Get_CategoriesToAdd()
    return Response({'message':'wada wada bn'})

@api_view(['POST','GET'])
def MEMBER_DETAILS_REGISTER(request,api_key):
    if (request.method == 'POST'):
        if API_KEY == api_key:
            member_serializer = MemberSerializer(data=request.data)
            try:
                if member_serializer.is_valid():
                    member_serializer.save()
                    authentication = Authentication_Info()
                    authentication.member = Member.objects.get(pk=member_serializer.data['user_name'])
                    authentication.is_registered = True
                    authentication.token = Get_token()
                    authentication.save()
                    return Response({'message':'Success !', 'token':authentication.token},status=status.HTTP_202_ACCEPTED)
                else:
                    if Member.objects.filter(pk=member_serializer.data['user_name']):
                        return Response(f'User Already Exsists !',status=status.HTTP_406_NOT_ACCEPTABLE)
            except KeyError:
                return Response(f'Invalid Data',status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response("API_KEY ERROR",status=status.HTTP_502_BAD_GATEWAY)

        
@api_view(['POST', 'GET'])
def CATEGORIES_COMMING(request,api_key,token):
    if API_KEY == api_key:
        member = Member.objects.get(pk = Authentication_Info.objects.get(token=token).member)
        if Fields.objects.filter(member = member):
            main_json = json.loads(json.dumps(request.data))
            main_json["member"] = Member.objects.get(pk=member)
            fields = Fields.objects.get(member=member)
            category_serializer = CategorySerializer(instance=fields, data=main_json)
            if category_serializer.is_valid():
                category_serializer.save()
                authentication = Authentication_Info.objects.get(member=member)
                authentication.token = Get_token()
                authentication.save(update_fields=['token'])
                print('updated')
                return Response({'message':'Success !', 'token':authentication.token , 'field':Get_CategoriesToAdd(member)},status=status.HTTP_202_ACCEPTED)
            else:
                return Response(f'Invalid Data',status=status.HTTP_401_UNAUTHORIZED)
        else:
            main_json = json.loads(json.dumps(request.data))
            main_json["member"] = Member.objects.get(pk=member)
            category_serializer = CategorySerializer(data=main_json)
            if category_serializer.is_valid():
                category_serializer.save()
                authentication = Authentication_Info.objects.get(member=member)
                authentication.token = Get_token()
                authentication.save(update_fields=['token'])
                return Response({'message':'Success !', 'token':authentication.token , 'field':Get_CategoriesToAdd(member)},status=status.HTTP_202_ACCEPTED)
            else:
                return Response(f'Invalid Data',status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response("API_KEY ERROR",status=status.HTTP_502_BAD_GATEWAY)


@api_view(['POST', 'GET'])
def MOBILE_COMMING(request,api_key,token):
    if API_KEY == api_key:
        if Authentication_Info.objects.filter(token=token):
            member = Member.objects.get(pk = Authentication_Info.objects.get(token=token).member)
            main_json = json.loads(json.dumps(request.data))
            main_json["member"] = Member.objects.get(pk=member)  
            if Mobile.objects.filter(member = member).exists() == False:
                mobile_serializer = MobileSerializer(data=main_json)
                if mobile_serializer.is_valid():
                    mobile_serializer.save()
                    authentication = Authentication_Info.objects.get(member=member)
                    authentication.token = Get_token()
                    authentication.save(update_fields=['token'])
                    return Response({'message':'Success !', 'token':authentication.token , 'field':Get_CategoriesToAdd(member)},status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(f'Invalid Data',status=status.HTTP_401_UNAUTHORIZED)
            else:
                mobile = Mobile.objects.get(member=member)
                mobile_serializer = MobileSerializer(instance=mobile , data=main_json)
                if mobile_serializer.is_valid():
                    mobile_serializer.save()
                    authentication = Authentication_Info.objects.get(member=member)
                    authentication.token = Get_token()
                    authentication.save(update_fields=['token'])
                    return Response({'message':'Success !', 'token':authentication.token , 'field':Get_CategoriesToAdd(member)},status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(f'Invalid Data',status=status.HTTP_401_UNAUTHORIZED)
                



















# @api_view(['POST','GET'])
# def MEMBER_DETAILS_REGISTER(request,api_key):
#     if (request.method == 'POST'):
#             if API_KEY == api_key:
#                 member_serializer = MemberSerializer(data=json.loads(json.dumps(request.data))['body-data']['member-data'])
#                 if member_serializer.is_valid():
#                     member_serializer.save()
#                     main_json = json.loads(json.dumps(request.data))['body-data']['category-data']
#                     main_json["member"] = Member.objects.get(pk=member_serializer.data['user_name'])
#                     category_serializer = CategorySerializer(data = main_json)
#                     if category_serializer.is_valid():
#                         category_serializer.save()
#                         return Response(f'success',status=status.HTTP_202_ACCEPTED)
#                     else:
#                         return Response('internal server error',status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#                 else:
#                     try:
#                         if member_serializer.errors.get("birthday")[0] == 'Date has wrong format. Use one of these formats instead: YYYY-MM-DD.':
#                             return Response(f'Birthday error',status=status.HTTP_406_NOT_ACCEPTABLE)
#                         else:
#                             return Response(f'Birthday error ekaknan na',status=status.HTTP_406_NOT_ACCEPTABLE)
#                     except:
#                         return Response(f'user already registered',status=status.HTTP_406_NOT_ACCEPTABLE)
#             else:
#                 return Response("API_KEY ERROR",status=status.HTTP_502_BAD_GATEWAY)
        