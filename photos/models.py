from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length =30)
    image = models.ImageField(max_length =60,upload_to='images/')
    description = models.TextField(max_length =200)

    
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news