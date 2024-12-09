"""
APIS APP
"""

from django.urls import path
from . import views 

app_name="apis"

urlpatterns = [

  path('', views.index,name="index"),

  # api views
  path('api/', views.book_list,name="book_list"),
  path('api/detail/<pk>/', views.book_detail,name="book_detail"),

  path('api/create/', views.book_create,name="book_create"),
  path('api/edit/<pk>/', views.book_update,name="book_update"),
  path('api/delete/<pk>/', views.book_delete,name="book_delete"),

]

