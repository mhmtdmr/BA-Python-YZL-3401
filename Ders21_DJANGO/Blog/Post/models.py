from datetime import datetime
from distutils.command.upload import upload
from statistics import quantiles
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Blog(models.Model):
    BlogID = models.AutoField(primary_key=True)
    BlogTitle = models.CharField(max_length=100)
    BlogText = models.TextField()
    BlogPublishDate = models.DateTimeField(default=datetime.now)
    BlogImage = models.ImageField(upload_to=f"images/post/%Y/%m/%d/",blank=True,default="NULL")
    BlogImage_238_134 = ImageSpecField(
        source='BlogImage',
        processors=[ResizeToFill(238,134)],
        format="JPEG",
        options={'quality':100}
    )

    def __str__(self):
        return self.BlogTitle
