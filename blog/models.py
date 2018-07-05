from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    content = models.TextField(max_length=1000)
    intTime = models.DateTimeField(auto_now_add=True)
    updTime = models.DateTimeField(auto_now=True)
    userId = models.IntegerField(null=False,default=0)