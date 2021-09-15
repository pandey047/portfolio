from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    desc=models.TextField()

    def __str__(self):
        return self.name+self.email




class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=300)
    content=RichTextUploadingField()
    # thumbnail=models.ImageField(null=True,blank=True,upload_to='images')
    slug=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title