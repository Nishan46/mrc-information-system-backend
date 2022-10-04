from django.urls import path
from . views import *

urlpatterns = [
    path('',Index,name='index'),
    path('member-register/<str:api_key>',MEMBER_DETAILS_REGISTER,name='MEMBER_DETAILS_REGISTER')
]
