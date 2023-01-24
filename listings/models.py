from django.db import models

# Create your models here.
def image_path(instance, filename):
    return f"listings/images{instance.id}/{filename}"

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    sqft = models.IntegerField()
    photo_main = models.FileField(upload_to=image_path) 
    photo_1 = models.FileField(upload_to=image_path, blank=True) 
    photo_2 = models.FileField(upload_to=image_path, blank=True) 
    photo_3 = models.FileField(upload_to=image_path, blank=True) 
    photo_4 = models.FileField(upload_to=image_path, blank=True) 
    photo_5 = models.FileField(upload_to=image_path, blank=True)  
    photo_6 = models.FileField(upload_to=image_path, blank=True)
    is_publushed = models.BooleanField(default=True)
    posted = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 
