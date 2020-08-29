from django.db import models
from tinymce.models import HTMLField
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import pytz
from tinymce.models import HTMLField

from PIL import Image


utc=pytz.UTC

# Create your models here.
class Field(models.Model):
    title=models.CharField('Pavadinimas',max_length=50,null=True)
    time=models.DateTimeField('Sukurta',null=True,auto_now=True)
    text=HTMLField('Tekstas',max_length=500,null=True)
    author=models.CharField(User,max_length=50,null=True)

    @property
    def cut_text(self):
        return self.text[:20]

    @property
    def comments_number(self):
        number=len(Comment.objects.filter(blog_id=self.pk))
        return number

    def __str__(self):
        return f"Pavadinimas: {self.title}/Laikas: {self.time}/Autorius: {self.author}"



class Comment(models.Model):
    blog_id=models.ForeignKey(Field,on_delete=models.SET_NULL,null=True,related_name='comment')
    email=models.EmailField('el.pastas',max_length=50,null=True,blank=True)
    time=models.DateTimeField('Sukurta',null=True, default=datetime.now)
    text=HTMLField('Komentaras',max_length=500,null=True)
    name=models.CharField('Vardas',max_length=50,null=True)

    def __str__(self):
        return f"Kas parase: {self.name}/Kada: {self.time}/Komentaras: {self.text}"


class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(default="default.png",upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self):
        super().save()
        img = Image.open(self.photo.path)
        if img.height > 200 or img.width > 200:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.photo.path)
