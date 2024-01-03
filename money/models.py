from django.db import models

# Create your models here.

def money_image_upload_path(instance, filename):
    # instance adalah instance dari model ScannerImage
    # filename adalah nama file yang diunggah

    # Menggunakan title dari instance sebagai bagian dari nama file
    title = instance.title
    # Mengganti spasi dengan garis bawah dan memastikan nama unik
    title = title.replace(" ", "_").lower()
    
    # Membangun path penyimpanan
    return f"money/image/bahan/{title}_{filename}"

class MoneyImage(models.Model):
    title = models.CharField(max_length=255)
    image_upload = models.ImageField(upload_to=money_image_upload_path, blank=True, null=True)
