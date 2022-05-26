from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    # article_image = models.ImageField(upload_to = 'articles/', blank=True, null=True)
   