from django.db import models

# Create your models here.

class CartoonImage (models.Model):
  image_upload = models.ImageField(upload_to='images/')
