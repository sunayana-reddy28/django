from django.urls import path
from .views import read_view
urlpatterns =[
    path("read/",read_view)
] 
