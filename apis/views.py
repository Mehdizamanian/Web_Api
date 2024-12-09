
from django.shortcuts import render , HttpResponse
from .models import Book

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer


# jinja views

def index(request):
  books=Book.objects.all()
  context={'books':books}
  return render(request,'apis/index.html',context)




# Api views

@api_view(['GET'])
def book_list(request):
    books=Book.objects.all()
    books_serializer=BookSerializer(books,many=True)
    return Response(books_serializer.data)


@api_view(['GET'])
def book_detail(request,pk):
  book=Book.objects.get(id=pk)
  book_serializer=BookSerializer(book,many=False)
  return Response(book_serializer.data)







@api_view(["POST"])
def book_create(request):
  serialized_data=BookSerializer(data=request.data)
  if serialized_data.is_valid():
    serialized_data.save()
  return Response(serialized_data.data)



@api_view(['POST'])
def book_update(request,pk):
   instance=Book.objects.get(id=pk)
   book_serializer=BookSerializer(instance=instance,data=request.data)
   if book_serializer.is_valid():
      book_serializer.save()
   return Response(book_serializer.data)





@api_view(["DELETE"])
def book_delete(request,pk):
   instance=Book.objects.get(id=pk)
   instance.delete()
   return Response("book deleted successfully .")