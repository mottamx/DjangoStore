# Generated by Django 4.2.3 on 2023-07-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/placeholder.jpg', upload_to='images/'),
        ),
    ]
