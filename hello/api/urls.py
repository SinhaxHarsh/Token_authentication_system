from django.contrib import admin
from django.urls import path
from home.views import PersonAPI,RegisterApi,LoginAPI

urlpatterns = [
    path('register/',RegisterApi.as_view()),
    path('persons/',PersonAPI.as_view()),
    path('login/',LoginAPI.as_view())
]
