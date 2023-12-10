from django.db import models

# Create your models here.

class CartoonImage (models.Model):
  image = models.ImageField(upload_to='cartoon_images/')
