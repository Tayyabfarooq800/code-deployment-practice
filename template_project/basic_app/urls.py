
from django.conf.urls import url
from django.urls import path
from basic_app import views

app_name = "basic_app"

urlpatterns = [
    
    url("other/" , views.other, name = "other"),
    url("relative/" , views.relative , name = "relative" ),


]