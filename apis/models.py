from django.db import models


class Book(models.Model):
  title=models.CharField(max_length=250)
  subtitle=models.CharField(max_length=250)
  author=models.CharField(max_length=250)
  isbn=models.CharField(max_length=250)
  #my extrafields
  description=models.TextField(blank=True,null=True)
  updated_time=models.DateTimeField( auto_now=True, auto_now_add=False)
  created_time=models.DateTimeField( auto_now=False, auto_now_add=True)
  status=models.BooleanField(default=True)

  def __str__(self):
    return self.title


# Create your models here.
