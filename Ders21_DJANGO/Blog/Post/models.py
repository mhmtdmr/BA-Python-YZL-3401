from datetime import datetime
from django.db import models

# Create your models here.
class Blog(models.Model):
    BlogID = models.AutoField(primary_key=True)
    BlogTitle = models.CharField(max_length=100)
    BlogText = models.TextField()
    BlogPublishDate = models.DateTimeField(default=datetime.now)
