from django.urls import path
from .views import *

urlpatterns = [
    path('',Index,name='index'),
    path('member-register/<str:api_key>',MEMBER_DETAILS_REGISTER,name='MEMBER_DETAILS_REGISTER'),
    path('category-comming/<str:api_key>/<str:token>',CATEGORIES_COMMING, name='CATEGORIES_COMMING'),
    path('mobile-comming/<str:api_key>/<str:token>',MOBILE_COMMING, name='CATEGORIES_COMMING')

]
