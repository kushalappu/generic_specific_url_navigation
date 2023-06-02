app_name='app3'
from django.urls import path
from app3.views import  *
urlpatterns = [
    path('sewag/',sewag,name='sewag'),
]