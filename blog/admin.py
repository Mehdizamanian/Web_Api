from django.contrib import admin
from .models import Post  , Category , Comment ,Tag


class PostAdmin(admin.ModelAdmin):
  list_display=['id','title','created_time','updated_time','active',]
  list_filter=['active']
  date_hierarchy='created_time'
  search_fields=('title','brif_description','description',)
  list_display_links=['id','title']

admin.site.register(Post,PostAdmin)


admin.site.register(Category)

admin.site.register(Tag)

class CommentAdmin(admin.ModelAdmin):
  list_display=['email','post','created_time','active',]

admin.site.register(Comment,CommentAdmin)

# Register your models here.