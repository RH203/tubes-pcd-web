from django.db import models
from django.utils import timezone

# Create your models here.
def cartoon_image_upload_path(instance, filename):
    # instance adalah instance dari model
    # filename adalah nama file yang diunggah

    # Menggunakan title dari instance sebagai bagian dari nama file
    title = instance.title
    # Mengganti spasi dengan garis bawah dan memastikan nama unik
    title = title.replace(" ", "_").lower()
    
    # Membangun path penyimpanan
    return f"cartoon/image/bahan/{title}_{filename}"

class CartoonImage (models.Model):
    title = models.CharField(max_length=255)
    image_upload = models.ImageField(upload_to=cartoon_image_upload_path, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)


    # untuk representasi teks yang jelas dari objek cartoon
    def __str__(self):
        return self.title