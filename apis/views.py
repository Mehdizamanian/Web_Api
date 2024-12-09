
from django.shortcuts import render , HttpResponse
from .models import Book



def index(request):
  books=Book.objects.all()
  context={'books':books}
  return render(request,'apis/index.html',context)

# Create your views here.
