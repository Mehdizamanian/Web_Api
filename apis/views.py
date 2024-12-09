from django.shortcuts import render , HttpResponse

def index(request):
  return render(request,'apis/index.html')

# Create your views here.
