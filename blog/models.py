from django.db import models



from django.db import models
from django.contrib.auth import get_user_model



user=get_user_model()


class Post(models.Model):
  title=models.CharField(max_length=250)
  brif_description=models.TextField()
  description=models.TextField()
  image=models.ImageField(upload_to='posts/images/',default='posts/images/1.png')
  updated_time=models.DateTimeField(auto_now=True, auto_now_add=False)
  created_time=models.DateTimeField(auto_now=False, auto_now_add=True)
  active=models.BooleanField(default=False)
  # relations
  author=models.ForeignKey(user,on_delete=models.CASCADE,blank=False)
  category=models.ManyToManyField("Category")
  tag=models.ManyToManyField("Tag")
  # slug=

  def __str__(self) -> str:
    return self.title


  class Meta:
    ordering=['-created_time']
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'







class Category(models.Model):
  title=models.CharField(max_length=100)
  
  def __str__(self):
    return self.title
  



class Comment(models.Model):
  post=models.ForeignKey(Post, on_delete=models.CASCADE)
  name=models.CharField(max_length=100)
  email=models.EmailField(max_length=254)
  message=models.TextField()
  active=models.BooleanField(default=False)
  created_time=models.DateField( auto_now_add=True)


  def __str__(self):
    return self.name


  class Meta:
    ordering=['-created_time',]




class Tag(models.Model):
  title=models.CharField(max_length=100)
  
  def __str__(self):
    return self.title
