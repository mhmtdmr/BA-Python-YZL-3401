from django.db import models

# Create your models here.
class News(models.Model):
    NewsID = models.AutoField(primary_key=True)
    NewsTitle = models.CharField(default="No Title",max_length=50)
    NewsBody = models.TextField()
