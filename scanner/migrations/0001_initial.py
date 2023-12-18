# Generated by Django 4.2.8 on 2023-12-18 15:09

from django.db import migrations, models
import scanner.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScannerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image_upload', models.ImageField(blank=True, null=True, upload_to=scanner.models.scanner_image_upload_path)),
            ],
        ),
    ]