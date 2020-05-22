from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models
User=get_user_model()



class SuccessStories(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    intro=models.TextField()
    description=RichTextUploadingField(null=True)
    image=models.ImageField(null=True,upload_to='SuccessStories')
    qoute=models.TextField()
    datePosted=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
