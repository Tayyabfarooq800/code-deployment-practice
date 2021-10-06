from django.urls import path
from basic_app import views
from basic_app.models import School , Student
from django.conf.urls import url

app_name = "basic_app"


urlpatterns = [
    path("" , views.SchoolListView.as_view() , name = "list"),
    path('<int:pk>/'  , views.SchoolDetailView.as_view() , name = "detail"),
]
