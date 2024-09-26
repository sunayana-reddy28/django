from django.shortcuts import render
from .models import Book

# Create your views here.
def read_view(request):
    output = Book.objects.all() # json format
    return render(request,"read.html",{"data":output})


