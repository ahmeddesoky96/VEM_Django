# Generated by Django 4.2.2 on 2023-06-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0003_alter_shop_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpicture',
            name='picture',
            field=models.ImageField(upload_to='build/static/product_images/'),
        ),
    ]
