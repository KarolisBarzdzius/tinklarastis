from django.contrib import admin
from .models import Field,Comment,Profile
# Register your models here.



class CommentAdmin(admin.ModelAdmin):
    list_display=('blog_id','name','time')

admin.site.register(Field)
admin.site.register(Comment)
admin.site.register(Profile)