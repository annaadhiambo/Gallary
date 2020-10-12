from django.db import models



# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length =30)
    image = models.ImageField(max_length =60,upload_to='images/')
    description = models.TextField(max_length =200)
    location = models.ForeignKey('Location',default='', on_delete = models.CASCADE)
    category = models.ForeignKey('Category',default='', on_delete = models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True, null = True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.delete()
        
    
    @classmethod
    def search_by_title(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__category__icontains=search_term)
        return images

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(max_length=200, null=True)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.delete()

    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    category = models.CharField(max_length=80, null= True)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.delete()

    def __str__(self):
        return self.category